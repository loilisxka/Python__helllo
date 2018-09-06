import math
qishiyear = input("请输入一个起始年月日")
zhongzhiyear= input("请输入一个终止年月日")
days = 1
xinyunri = 0
for years in range(int(qishiyear[0:4]),int(zhongzhiyear[0:4])):
    for mouth in range(1,13):
        if mouth == 1:
            day = 31
        elif mouth == 2:
            if (years %4 ==0 and years %100 !=0) or years %400 == 0:
                day = 29
            else:
                day = 28
        elif mouth == 3:
            day =31
        elif mouth == 4:
            day = 30
        elif mouth == 5:
            day = 31
        elif mouth == 6:
            day = 30
        elif mouth == 7:
            day = 31
        elif mouth == 8:
            day = 31
        elif mouth == 9:
            day = 30
        elif mouth == 10:
            day = 31
        elif mouth == 11:
            day = 30
        elif mouth == 12:
            day = 31
        days += day
        if days%7 ==0 and years >1900:
            xinyunri +=1
print (xinyunri)
                   
