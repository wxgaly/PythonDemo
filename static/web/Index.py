"""
   date: 2018-03-07 0:14 
"""

__author__ = "WXGALY"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 导入我们自己编写的application函数:

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
