# -*- coding: utf-8 -*-
import time,functools
def metric(text):
    def decorator(fn):
        @ functools.wraps(fn)#把原始函数的__name__等属性复制到warpper中
        def warpper(*args,**kw):#当中的变量就是fn中的变量
            print('%s executed in %s ms'%(fn.__name__,10.24))
            return fn(*args,**kw)
        return warpper
    return decorator
#测试
@metric('execute')
def fast(x,y):
    time.sleep(0.0012)
    print(x+y)
    return x+y;

@metric('execute')
def slow(x,y,z):
    time.sleep(0.1234)
    print(x*y*z)
    return x*y*z;
f = fast(11,22)
s = slow(11,22,33)
if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')