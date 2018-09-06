# -*- coding: utf-8 -*-
def is_palindrome(n):
    a = 0
    if n < 10 :
        return True
    else:
        n = str(n)
        for i in range(1,len(n)+1):
            a = a*10 + int(n[-i])
        if int(n) / float(a) == 1:
            return True
#测试
output = filter(is_palindrome,range(1,1000))
print('1~1000',list(output))
if list(filter(is_palindrome,range(1,200))) == [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]:
    print('测试成功！')
else:
    print('测试失败！')