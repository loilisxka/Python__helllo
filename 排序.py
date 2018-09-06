# -*- coding: utf-8 -*-
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    a = t[0]
    return a
'''L2 = sorted(L,key = by_name)
print(L2)'''
def by_score(t):
    a = t[1]
    return a
L2 = sorted(L,key = by_score,reverse = True)
print(L2)