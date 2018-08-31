# mini_web模块，能够处理用户的动态请求
# 1. 模板替换
# 2. 路由

import datetime
from pymysql import connect
import re


# 这个列表里面放着元组 "请求路径":<处理方法函数对象>
# route_list = list()
# 我在想处理成字典会不会更快呢！
# 但占用更大的内容空间!
route_list = dict()


def route(url):
    """路由方法"""

    def decorator(func):
        """装饰器"""

        def wrapped_func(*args, **kwargs):
            """实现新功能代码"""
            return func(*args, **kwargs)

        route_list[url] = wrapped_func
        return wrapped_func

    return decorator


def application(data_dict):
    """
    传入的参数是一个字典，目前只存放一个值，env
    :param data_dict: 访问路径
    :return response_header, response_para , response_body
    """

    # 一些固定的参数
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header_para = "Content-Type:text/html; charset=utf-8\r\n\r\n"
    # response_body = "<h1>欢迎来主页</h1>"

    # 获得请求
    PATH = data_dict["PATH_INFO"]

    # 使用路由处理请求
    try:
        func = route_list[PATH]
        return response_header, response_header_para, func()
    except KeyError:
        response_header = "HTTP/1.1 400 NOT FOUND\r\n"
        response_header_para = "Content-Type:text/html; charset=utf-8\r\n\r\n"
        response_body = "<h1>网页建设中</h1>"
        return response_header, response_header_para, response_body


# ===========================================以上框架=====================================================

def get_data(database, sql):
    """操作数据库的方法"""
    # 为什么直接connect方法用with返回游标对象？
    with connect(host="192.168.255.130", user="python", password="123456", database=database, port=3306,
                 charset='utf8') as c:
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return data


@route("/time.html")
def time():
    return "<h1>现在的时间为<br>{}</h1>".format(datetime.datetime.now())


@route("/index.html")
def index():
    # 1. 读取前段内容
    # 2. 读取数据库内容
    # 3. 替换内容
    # 4. 打包发送

    # 1. 读取前端内容
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()

    # 2. 读取数据库内容
    sql = """select * from info;"""
    data = get_data("stock_db", sql)

    # 3. 替换内容
    row = """
            <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
            <td>{5}</td>
            <td>{6}</td>
            <td>{7}</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
            </td>
            </tr>
            """
    rows = ""
    for info in data:
        rows += row.format(*info)

    # 4. 打包发送
    new_content = re.sub(r"{%content%}", rows, content)
    return new_content


@route("/center.html")
def center():
    # 1. 读取前段内容
    # 2. 读取数据库内容
    # 3. 替换内容
    # 4. 打包发送

    # 1. 读取前端内容
    with open("./templates/center.html", encoding="utf-8") as f:
        content = f.read()

    # 2. 读取数据库内容
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info 
             from info as i inner join focus as f on i.id = f.info_id;"""

    data = get_data("stock_db", sql)

    # 3. 替换内容
    row = """
            <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/300280.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300280">
            </td>
            </tr>"""
    rows = ""
    for info in data:
        rows += row.format(*info)

    # 4. 打包发送
    new_content = re.sub(r"{%content%}", rows, content)
    return new_content


@route("/300280.html")
def update():
    with open("./templates/update.html", encoding="utf-8") as f:
        content = f.read()
        return content