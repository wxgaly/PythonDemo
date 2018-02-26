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

from io import StringIO

f = StringIO()

f.write("hello")

print(f.getvalue())
