# -*- coding: utf-8 -*-
from enum import Enum,unique
@unique#检查枚举类中是否有重复项
class Gender(Enum):#自定义一个枚举类
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
#测试
bart = Student('Bart',Gender(0))
if bart.gender == Gender.Male:#这里的Gender为之前自定义的枚举类，而bart.gender为Student类的self.gender
    print('测试通过！')
else:
    print('测试失败！')
#这中的gender有多种含义，一定要分清