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


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)

print(x, y)
