import math
a = float(input("请输入三角形一条边的长度:"))
b = float(input("请输入三角形一条边的长度:"))
c = float(input("请输入三角形一条边的长度:"))
d = (a**2+b**2-c**2)/2*a*b
print ("角度为%.1f"%(math.acos(d)*180/math.pi))
