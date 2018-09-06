import math
def hannorta(n,A,B,C):
    if n == 1:
        print ("将第",n,"个盘子从",A,"移动到",C,"上")
    else:
        hannorta(n-1,A,C,B)
        print ("将第",n,"个盘子从",A,"移动到",C,"上")
        hannorta(n-1,B,A,C)
n = int(input("请输入盘子的个数"))
hannorta(n,"left","mid","right")
