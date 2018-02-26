"""
    
    date: 2018-02-26 16:14
"""

__author__ = "WXGALY"

# 读写文件 r为读，w为写

# with open("E:/demo-code/PythonDemo/static/IODemo.py", "w") as f:
#     # print(f.read())
#     # for line in f.readlines():
#     #     print(line.strip())
#     f.write('Hello, world!')


# StringIO and ByteIO
# from io import StringIO
#
# f = StringIO()
#
# f.write("hello")
#
# print(f.getvalue())

# from io import BytesIO
#
# f = BytesIO()
#
# f.write('中文'.encode("utf-8"))
#
# print(f.getvalue())


# 操作文件和目录

import os

# print(os.name)
# print(os.uname())  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# print(os.environ.get('PATH'))

# print(os.path.abspath("."))

# print(os.path.join(os.path.abspath("."), "test"))

# path = os.path.join(os.path.abspath("."), "test")

# os.mkdir(path)

# os.rmdir(path)

path = 'D:/Code/intellij_workspace/PythonDemo/static/'
name = 'IODemo.py'

# print(os.path.split(path + name))
# print(os.path.splitext(path + name))

# os.rename()
# os.remove()

# print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
