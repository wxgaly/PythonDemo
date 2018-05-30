"""
   date: 2018-05-26 22:35 
"""
import math

__author__ = "WXGALY"


# a = 91
# b = 2
# c = a + b
#
# name = '李妍'
#
# print(b, a)
# print("a=", a, b, c)
# print("b =", b)
# print("c =", c)
# print("name =", name)
#
# print("--------")
#
# if a < 60:
#     print("不及格")
# elif a <= 70:
#     print("D")
# elif a <= 80:
#     print("C")
# elif a <= 90:
#     print("B")
# else:
#     print("A")

# list
# names = ['Michael', 'Bob', 'Tracy', 1, 1.2]

# for name in names:
#     print(name)

# i = 1
# while i < len(names):
#     print(names[i])
#     i += 2

# ints = list(range(5))
#
# for integer in ints:
#     print(integer)

# sum = 0


# def customRange(n):
#     list1 = []
#     i = 0
#     while i < n:
#         list1.append(i)
#         i += 1
#     return list1


# for x in range(101):
#     sum += x


# for x in customRange(1001):
#     sum += x
#
# print(sum)

# def area_of_circle(r):
#     return 3.14 * r * r
#
#
# print(area_of_circle(6))

# names = ['1', '2', 3, 4.5]
#
# for name in names:
#     print(name)

#
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Tracy'])
# print(d.get('a'))


# def quadratic(a, b, c):
#     temp = pow(b, 2) - 4 * a * c
#     if temp < 0:
#         return "无解"
#     else:
#         return (-b + math.sqrt(temp)) / (2 * a), (-b - math.sqrt(temp)) / (2 * a)
#
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
# print('quadratic(1, 3, -4) =', quadratic(1, 1, 1))
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')
# # for key in d.keys():
#     print(key, d[key])

# for value in d.values():
#     print(value)

# class Person:
#     name = 'zhangsan'
#     age = 18
#     sex = 'male'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self, food):
#         print(self.name, food)
#
#
# person1 = Person("lisi", 13, 'male')
# person2 = Person("wangwu", 15, 'female')
#
# print(person1.eat("面包"))
#
# print(person2.eat("鸡蛋"))
# def mymax(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
#
# print('mymax(4, 6)=',mymax(4, 6))
# def myfbnq(n):
#     if n<=0:
#         return "无效"
#     elif n<4:
#         return n
#     elif n==4:
#         return n+1
#     else:
#         return 2*(n-4)+3*(n-3)
#
#
# print('myfbnq(3) =', myfbnq(7))

# 循环形式实现
# def fbnq(n):
#     if n <= 0:
#         return "无效"
#     elif n <= 2:
#         return n
#     else:
#         n2 = 1
#         n1 = 2
#         x = 3
#
#         while n > 2:
#             x = n1 + n2
#             n2 = n1
#             n1 = x
#             n -= 1
#
#         return x

# def fbnq(n):
#     if n == 1:
#         return 1
#
#     if n == 2:
#         return 2
#
#     return fbnq(n - 1) + fbnq(n - 2)

def mypow(x, y):
    if y < 0:
        return "无解"
    if y == 0:
        return 1

    if y == 1:
        return x

    return mypow(x, y - 1) * x


print(' mypow(2, 100)=', mypow(2, 100))

# def myPow(x, y):
#     temp1 = x
#     temp2 = 0
#
#     while y > 1:
#         temp2 = x * temp1
#         temp1 = temp2
#         y -= 1
#
#     return temp2
#
#
# print(myPow(2, 10))
