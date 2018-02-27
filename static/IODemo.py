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

# import os

# print(os.name)
# print(os.uname())  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# print(os.environ.get('PATH'))

# print(os.path.abspath("."))

# print(os.path.join(os.path.abspath("."), "test"))

# path = os.path.join(os.path.abspath("."), "test")

# os.mkdir(path)

# os.rmdir(path)

# path = 'D:/Code/intellij_workspace/PythonDemo/static/'
# name = 'IODemo.py'

# print(os.path.split(path + name))
# print(os.path.splitext(path + name))

# os.rename()
# os.remove()

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


# 序列化
# import pickle
#
# path = "C:/Users/Administrator/Desktop/a.txt"

# with open(path, 'wb') as f:
#     d = dict(name='Bob', age=20, score=88)
#
#     pickle.dump(d, f)

# with open(path, "rb") as f:
#     d = pickle.load(f)
#     print(d)


# Json

import json


# d = dict(name='Bob', age=20, score=88)
#
# print(json.dumps(d))

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#
# print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


stu = Student('xiaoming', 18, 90)

jsonStr = json.dumps(stu, default=lambda obj: obj.__dict__)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


stu = json.loads(jsonStr, object_hook=dict2student)

print(stu.name)

