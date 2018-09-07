# -*- coding: utf-8 -*-
from functools import reduce#引入reduce函数
def str2num(s):
    try:
        return int(s)
    except ValueError as e:#处理错误：当无法返回一个整数值时，执行如下语句
        return float(s)
def calc(exp):
    ss = exp.split('+')#将输入的字符串以+号为断点，划分字符串
    ns = map(str2num,ss)#以map函数重新输出一个列表
    return reduce(lambda acc, x: acc + x, ns)#将列表中所有的项相加
def mian():
    r = calc('100 + 200 +345')
    print('100 + 200 + 345 =',r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =',r)
mian()#执行mian()函数