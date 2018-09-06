# -*- coding: utf-8 -*-
from collections.abc import Iterable
def findminandmax(L):
    max = 0
    if isinstance(L,Iterable) == True:
        min = L[0]
        for i in L:
            if i > max:
                max = i
            elif i < min :
                min = i
            else:
                continue
        return max,min
    else:
        return None,None
L = [1,2,3,4,5]
print(findminandmax(L))
