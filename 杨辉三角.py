# -*- coding: utf-8 -*-
def yanghui(n):
    L = [1]
    while len(L) <= n:
        yield L
        L = [L[0]]+[(L[i]+L[i+1]) for i in range(len(L)-1)]+[L[-1]]
n = int(input(':'))
for n in yanghui(n):#前面一个n代表的是每次的yield L ,后面一个n是我输入的行数
    print(n)