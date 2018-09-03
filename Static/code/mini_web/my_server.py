# 小型的服务器，能够将接收到的数据处理给mini_web处理
# 先打补丁
import sys

from gevent import monkey

monkey.patch_all()

import gevent
import socket
import re


class MyServer(object):
    """小型服务器的类"""

    def __init__(self, port):
        """初始化服务器对象的参数，主要是设置tcp_socket，得到的服务器对象作为私有属性"""
        # 创建socket对象，tcp的
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置端口复用 - 端口复用在绑定之前
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 绑定端口
        self.__server.bind(("", port))

        # 设置监听
        self.__server.listen(128)

    def run(self):
        """run方法，能够使得服务器对象去循环监听客户端的请求"""
        while True:
            # 接受客户端请求
            client_socket, client_addr = self.__server.accept()

            # 开启协程去处理用户的请求  # PS这里面如果要开进程怎么处理？
            gevent.spawn(self.handle_client, client_socket)

        # 关闭服务器
        self.__server.close()

    # 设置成静态方法的原因是它完全用不到任何和实例相关的资源，
    # 但是确实是服务器的一个重要的方法，必须封装在类的内部
    @staticmethod
    def handle_client(client_socket: socket.socket):
        """服务器处理客户端的请求
        1. 如果访问静态资源，直接发送过去
        2. 访问动态资源将交给mini_web去处理
        """

        # 获得请求头
        # 1kb内容？1024字节应该够了。tcp20个字节
        request_header = client_socket.recv(1024).decode("utf-8")

        # 获得请求路径
        # GET / HTTP/1.1
        # 因为有可能是POST所以在处理正则的时候可以这么写
        # 不是浏览器请求直接关闭连接
        try:
            request = re.search(r'\w{3,4} (.*) HTTP/1.1', request_header).group(1)
        except:
            return

        print(request)

        # 处理请求
        # 0. 准备相应头和参数
        # 1. 如果是/ 直接跳转到主页
        # 2. 静态文件， 发送
        # 3. html文件，交给mini_web

        #  判断请求, 动态请求的话交给mini_web 处理
        if request == "/":
            # 1. 如果用户没有指定资源路径那么默认访问主页
            request = "/index.html"

        if request.endswith(".html"):
            # 2. mini_web处理动态请求
            # 明天听一下这里是怎么处理的
            # TODO:为什么要处理成字典？
            env = {
                "PATH_INFO": request
            }
            import mini_web
            response_header, response_header_para, response_body = mini_web.application(env)
            client_socket.send((response_header + response_header_para + response_body).encode("utf-8"))
        else:
            # 3. 处理静态文件
            try:
                # 发送文件
                with open("./static" + request, "rb") as f:
                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header_para = "Content-Type\r\n\r\n"
                    client_socket.send((response_header + response_header_para).encode("utf-8"))
                    while True:
                        content = f.read(1024)
                        if not content:
                            break
                        client_socket.send(content)
            except IOError:
                # 没找到文件发送失败
                response_header = "HTTP/1.1 404 NOT FOUND\r\n"
                response_header_para = "Content-Type:text/html; charset=utf-8\r\n\r\n"
                response_body = "<h1>抱歉，访问的网站不存在</h>"
                client_socket.send((response_header + response_header_para + response_body).encode("utf-8"))
            finally:
                # 关闭客户端socket即使释放资源
                # TODO:为什么要在发送文件后关闭？
                client_socket.close()


def main():
    """服务器主程序"""
    # 要能根据参数设置端口
    command_list = sys.argv
    if len(command_list) != 2:
        print("语法: python3 路径 端口")
        return
    else:
        try:
            port = int(command_list[1])
        except:
            print("语法: python3 路径 端口")
            return

    # 1. 创建服务器
    server = MyServer(port)
    # 2. 启动服务器
    server.run()


if __name__ == '__main__':
    main()
