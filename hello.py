# -*- coding: utf-8 -*-
L1 = ['hello','world',18,'apple',None]
L2 = [a for a in L1 if isinstance(a,str) == True]
print(L2)