# -*- coding: utf-8 -*-
import itertools
def pi(n):
    a = 0
    jishu = itertools.count(1,2)
    xulie = list(itertools.takewhile(lambda x: x <= 2*n-1 ,jishu))
    for i in range(len(xulie)):
        if i % 2 != 0:
            b = 4./-xulie[i]
        else:
            b = 4./xulie[i]
        a = b + a
    return a
#测试
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 <pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')