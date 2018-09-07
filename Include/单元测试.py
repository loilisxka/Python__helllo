# -*- coding: utf-8 -*-
import unittest#引入unittest模块

class Student(object):

    def __init__(self,name,score):#进行赋值
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 60 and self.score <= 79:
            return 'B'
        elif self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score <= 59 and self.score >= 0:
            return 'C'
        else:
            raise ValueError#发出错误

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):#测试80到100之间类是否能正常运行
        s1 = Student('Bart',80)
        s2 = Student('Lisa',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assretEqual(s2.get_grade(),'A')

    def test_60_to_80(self):#测试60到80之间类是否能正常运行
        s1 = Student('Bart',60)
        s2 = Student('Lisa',79)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(),'B')

    def test_0_to_60(self):#测试0到60之间类能否正常运行
        s1 = Student('Brat',0)
        s2 = Student('Lisa',59)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'C')

    def test_invalid(self):#测试0到60之间类能否正常运行
        s1 = Student('Bart',-1)
        s2 = Student('Lisa',101)
        with self.assertRaises(ValueError):
            s1.get_grade()#输出错误
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()