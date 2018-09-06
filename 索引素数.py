def prime(n):
    sushu_list = []
    if n == 1:
        return False
    for i in range(2,n):
        for c in range(2,i):
            if i % c == 0:'''如果在这里判断不等于的情况并且把i
写到sushu_list的话，将会出错。比如9，在本循环中，第一次9除以2就
会除不尽，会把9写进sushu_list。这一程序就出错了'''
                break
        else:
            sushu_list.append(i)

    return sushu_list
def bi_search(n,x):
    sushu_list = prime(n)
    low = 0
    high = len(sushu_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if sushu_list[mid] == x:
             return mid
        elif sushu_list[mid] > x:
             high = mid - 1
        else:
             low = mid + 1
    return -1
n = int(input("请输入一个整数"))
lst = []
shuchu_list = []
for z in range(5):
    lst.append(int(input("请输入几个小于n整数")))

for x in lst:
    shuchu_list.append(bi_search(n,x))
print (shuchu_list)
'''print(prime(10))'''


    
                
