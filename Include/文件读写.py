# -*- coding: utf-8 -*-
fpath = r'C:\windows\system.ini'

with open(fpath,'r') as f:
    s = f.read()
    print(s)