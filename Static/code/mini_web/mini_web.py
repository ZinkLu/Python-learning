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
