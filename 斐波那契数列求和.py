import math



def shulei(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return shulei(n-1)+shulei(n-2)
shuzi = int(input("请输入一个数"))
a = 0
n = 1
while shuzi > 0:
    
    if shuzi > shulei(n)and shulei(n) % 2 == 0:
        a += shulei(n)
        n += 1
    elif shuzi > shulei(n) and shulei(n) % 2 != 0:
        n += 1
    else:
        print (a)
        break
else:
    print ("请输入一个正整数")


    
    
