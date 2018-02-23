# list 有序链表（可修改元素）
# names = ["zhangsan", 1, "wangwu"]
# a = ["a", 2.0]

# names.append(a)
# names.insert(1, "hah")

# print("before names: ", names)

# names.pop()
# print("after names: ", names)

# tuple 有序元组（不可修改元素）
# classes = {"class one", "class two"}

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# for循环
# for name in names:
#     print(name)
#
# for cls in classes:
#     print(cls)

# sum = 0
#
# for i in range(101):
#     sum += i
# print(sum)

# dictionary字典即java中的map
# d = {'a': 1, "b": 2}
# print(d["a"])
#
# d["a"] = 10
#
# print(d["a"])

# set 不存在重复的元素
# s = set([1, 2, 2, 3, 3])
# print(s)

# 调用函数

# def max2(x, y):
#     if x >= y:
#         return x
#     else:
#         return y
#
#
# print(max2(1, 2))

import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
#
# print(x, y)

#
# def square(a):
#     return a * a
#
#
# def quadratic(a, b, c):
#     x = (-b + math.sqrt(square(b) - 4 * a * c)) / 2 * a
#     y = (-b - math.sqrt(square(b) - 4 * a * c)) / 2 * a
#     return x, y
#
#
# x, y = quadratic(3, 4, -5)
#
# print(x, y)

# 函数默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n -= 1
#         s *= x
#     return s
#
#
# print(power(5))
# print(power(5, 3))
# print(power(5, n=4))

# 可变参数，即将参数作为list或者tuple传入

# def calc(numbers):
#     s = 0
#     for n in numbers:
#         s += n
#     return s
#
# def calc1(*numbers):
#     s = 0
#     for n in numbers:
#         s += n
#     return s
#
#
# print(calc([1, 2, 3]))
#
#
# nums = {1, 2, 5}
# print(calc1(*nums))

# 递归函数

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(50))

# 高级特性

# 切片
# L = ["a", "b", "c", "d"]
#
# print(L[0:3])
#
# L = list(range(100))
#
# # 前十个数，每个2个取一个
# print(L[:10:2])

# 迭代
# L = ["a", "b", "c", "d"]

# for x in L:
#     print(x)

# dicts = {'a': 1, 'b': 2, 'c': 3}

# for k in dicts.keys():
#     print(k)

# for v in dicts.values():
#     print(v)

# for k, v in dicts.items():
#     print(k, v)

# 以下标形式迭代
# for i, v in enumerate(L):
#     print(i, v)

# for x, y in [(1, 2), (2, 3), (3, 4)]:
#     print(x, y)


# 列表生成器
# L = [x * x for x in range(1, 11)]
# print(L)

# import os

# 遍历当前文件夹下的文件名
# print([d for d in os.listdir('.')])


# 生成器 使用()包裹，或者使用yield关键字

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield (b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# for i in fib(5):
#     print(i)


# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的
#
#
# from collections import Iterable
#
# print(isinstance([], Iterable))
#
# print(isinstance(100, Iterable))
#
# from collections import Iterator
#
# print(isinstance((x for x in range(10)), Iterator))
