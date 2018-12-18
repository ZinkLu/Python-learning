# -*- coding: utf-8 -*-
# 2018-12-18
# author: ShuyangLu
# 能够生成不同格式的cdkey, 检查唯一性, 并且写入数据库(默认是postgresql)

import string
import random
import psycopg2

def mani(cr, cdkey_count, cdkey_len, cdkey_format='num'):
    """随机生成激活码
    param: 
    cr 数据库游标对象
    cdkey_count: 生成多少个cdkey
    cdkey_len: cdkey的长度
    cdkey_format: cdkey的格式, 支持'num'和'num+letter'
    """
    if cdkey_format not in ('num', 'num+letter'):
        raise ValueError("仅支持生成纯数字(num), 和数字+字母(num+letter)的组合")

    digit_string = list(string.digits)
    upper_letters = list(string.ascii_uppercase)

    if cdkey_format == 'num_letter':
        random_pool = set(digit_string + upper_letters)
        confusions = {'l', 'L', 'I', 'i', 'o', 'O', 'z', 'Z'}  # 去除一些容易搞混淆的字母
        random_pool.difference_update(confusions)
        random_pool = list(random_pool)
    else:
        random_pool = digit_string

    # 生成cdkey
    amount_remain = cdkey_count
    conflit_count = 0
    max_size = 50
    while amount_remain > 0:
        to_generate = max_size if amount_remain > max_size else amount_remain
        cdkeys = [''.join([random.choice(random_pool) for _ in xrange(cdkey_len)]) for _ in xrange(to_generate)]

        # 万一随机生成了重复的激活码, 则去重
        cdkeys = set(cdkeys)

        # 检查重复cdkeys
        # TODO: 改为自己的数据库
        cdkeys_count_sql = """
            SELECT x FROM ******* WHERE x IN %(cdkeys)s
        """
        cr.execute(cdkeys_count_sql, {'cdkeys': tuple(cdkeys)})
        cdkeys_exists = cr.fetchall()

        # 记录下当前的冲突总数, 下一次循环也需要检查冲突数, 这一句话可以不用写, 写了再多次生成时候更加安全
        conflit_count += len(cdkeys_exists)

        # 重复过多, 需要提高位数
        if conflit_count >= amount_remain * 0.9:
            raise Exception(u'警告', u'%d位的授权码即将耗尽, 请尝试更长位数的授权码或减少生成个数' % cdkey_len)

        # 允许存在少量冲突, 先去重再进行生成
        cdkeys_exists_set = {cdkey[0] for cdkey in cdkeys_exists}
        cdkeys.difference_update(cdkeys_exists_set)
        cdkeys_sql = """
            INSERT INTO ******
                (create_uid, create_date, write_uid, write_date, name, used)
            VALUES
                %s
        """
        cdkeys_sql_list = ["(%s, now(), %s, now(), '%s', False)" % (uid, uid, cdkey) for cdkey in cdkeys]
        cr.execute(cdkeys_sql % ','.join(cdkeys_sql_list))

        # 计算出还需生成的数量, 进入下一次循环
        amount_remain -= len(cdkeys)


if __name__ == "__main__":
    conn = psycopg2.connect(dbname = 'xxx', user='xxx')
    cr = connt.cursor()
    main(cr, 10, 4, 'num')
    cr.close()
    conn.close()
