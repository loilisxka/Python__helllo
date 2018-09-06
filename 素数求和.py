n = int(input("请输入一个数:"))
a = 0
for i in range(2,n):#找一个1到n之间的数i
    for b in range(2,i):#判断这个i是否为素数
        if i % b == 0:
          break
    else:#由于需要找个i出来+=所以应该于第二个for出于同一级别
        a += i
print (a)
