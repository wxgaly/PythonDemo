"""
    面向对象编程
"""

__author__ = 'WXGALY'

# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_age(self):
#         print('%s: %s' % (self.name, self.age))
#
#     def get_grade(self):
#         if self.age >= 20:
#             return 'A'
#         elif self.age >= 40:
#             return 'B'
#         else:
#             return 'C'
#
#
# stu1 = Student("bb", 14)
#
# print(stu1.get_grade())


# 枚举类型

from enum import Enum, unique

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun

print(day1)
