import math
n = int(input("请输入一个正整数"))
a = 0#定义一个存储和的变量
for i in range(1,n):#利用循环穷举1到n之间的数字
    if i % 3 == 0 or i % 5 == 0:#利用逻辑关系取出需要的i值
        a += i
print (a)
     
    
