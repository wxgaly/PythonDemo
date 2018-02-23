"""
    面向对象编程
"""

__author__ = 'WXGALY'


# Student 类继承自object

# class Student(object):
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     def print_age(self):
#         print('%s: %s' % (self.__name, self.age))
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

# print(stu1.get_grade())

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
# print(stu1._Student__name)

# 使用type函数来确定一个对象的类型

# print(type(1))
#
# print(type(stu1))

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# def readData(fp):
#     return getattr(fp, 'read')
#
#
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

# 使用__slots__去限制绑定属性


class Student(object):
    # __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth

    def __str__(self):
        return 'Student object (_birth: %s)' % self._birth

    __repr__ = __str__


stu = Student()
stu.birth = 1994

print(stu)

