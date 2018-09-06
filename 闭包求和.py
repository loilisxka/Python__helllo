# -*- coding: utf-8 -*-
def createCounter():
    n = 0
    def counter():
        nonlocal n#nonlocal指令是从内部改变外层的值（这里外层n的值被替换了）
        #同理不能在counter里面赋值一个n（如n=1），因为每次调用是输出counter，所以默认每次重新赋值n
        n = n + 1
        return n
    return counter
#测试
counterA = createCounter()
print (counterA(),counterA(),counterA(),counterA(),counterA())
counterB = createCounter()#由于counterA和counterB是两个函数所以这二者内部的n被重新赋值为零
if [counterB(),counterB(),counterB(),counterB()] == [1,2,3,4]:
    print('测试通过！')
else:
    print('测试失败！')
#本题不能在函数外部定义一个全局变量n，这样在调用counterA和counterB时n的值不会被重新赋值为零，而是继续叠加下去。