# -*- coding: utf-8 -*-
L = [6,4,3,8,1,7,9,2]
for i in range(len(L)//2):#设置循环次数，对L的长度进行整除以2
    swap_flag = False#设置一个交换的标记，这里默认没有进行交换
    for a in range(i,len(L)-i-1):#先正向进行一次排序，把最大的放到最后
        if L[a] > L[a+1]:
            L[a] , L[a+1] = L[a+1] , L[a]
    for b in range(len(L)-2-i,i,-1):#后进行一次逆向排序，同样的将较大的数字拿上来
        if L[b] < L[b-1]:
            L[b] , L[b-1] = L[b-1] , L[b]
            swap_flag = True#两次循环之后，把交换标记置为True（意为：已经交换完毕）
    if not swap_flag:#如果没有执上方两次循环，则交换标记仍未False
            break#打断本次循环，即所有数字已经排序完毕
#鸡尾酒排序，即为从前到后，再从后到前，同时进行两次循环，比一般的排序更快。
print(L)