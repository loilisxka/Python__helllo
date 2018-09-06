#年月日
year = input("请输入代表时间的八位数:")
str(year)
if len(year) == 8 :
    print (year[0:4]+'年'+year[4:5]+'月'+year[-2:]+'日')
else:
    print("输入有误")
          
