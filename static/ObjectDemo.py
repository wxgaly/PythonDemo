"""
    面向对象编程
"""

__author__ = 'WXGALY'


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))

    def get_grade(self):
        if self.age >= 20:
            return 'A'
        elif self.age >= 40:
            return 'B'
        else:
            return 'C'


stu1 = Student("bb", 14)

print(stu1.get_grade())
