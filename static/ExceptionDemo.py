"""
    异常处理
"""

__author__ = 'WXGALY'

# 异常处理，与java等高级语言类似，通过try语句
#
# import logging

#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
#
# main()
# print('END')


# 自定义异常

# class FooError(ValueError):
#     pass
#
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
#
# foo('0')

# from functools import reduce
#
#
# def str2num(s):
#     return int(s)
#
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     try:
#         r = calc('100 + 200 + 345')
#         print('100 + 200 + 345 =', r)
#         r = calc('99 + 88 + 7.6')
#         print('99 + 88 + 7.6 =', r)
#     except ValueError as e:
#         logging.log(logging.ERROR, e)
#
#
# main()


# 单元测试

import unittest


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if 60 <= self.score < 80:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()
