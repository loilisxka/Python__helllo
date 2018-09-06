import math
def runnian(c):
    if (c % 4 == 0 and c % 100 != 0) or c % 400 == 0:
        return 1
    else:
        return 0
def days(mouth,year):
    if mouth in (1,3,5,7,8,10,12):
        return 31
    elif mouth in (4,6,10,11):
        return 30
    else:
        if runnian(c) == 1:
            return 29
        else:
            return 28
year = int(input("请输入一个年份的数字"))
mouth = int(input("请输入一个上述年份中的月份"))
over_year_day=0
a=0
now_day=0
if year > 1800:
    for c in range(1800,year):
        if runnian(c) == 1:
            a += 1
        else:
            continue
    over_year_day = (year - 1800)*365 + a
elif year == 1800:
    over_year_day = 0
else:
    print("抱歉我还没有办法计算这么古老的时间点哦")
for mouth in range(1,mouth+1):
    now_day += days(mouth,year)
allday = now_day + over_year_day
if (allday - 5) % 7 == 0:
    print (year,"年",mouth,"最后一天是星期日")
elif (allday - 5) % 7 == 1:
    print (year,"年",mouth,"最后一天是星期一")
elif (allday - 5) % 7 == 2:
    print (year,"年",mouth,"最后一天是星期二")
elif (allday - 5) % 7 == 3:
    print (year,"年",mouth,"最后一天是星期三")
elif (allday - 5) % 7 == 4:
    print (year,"年",mouth,"最后一天是星期四")
elif (allday - 5) % 7 == 5:
    print (year,"年",mouth,"最后一天是星期五")
else:
    print (year,"年",mouth,"最后一天是星期六")
    
    
        
