import math
ch = ''#定义一个无关变量
while ch != 'q':
      miaoshu = int(input("请输入一个秒数:"))#将输入的秒数转化为整数型
      if miaoshu<0 :
          print  ("输入有误")
      else :
          a = miaoshu//3600
          b = (miaoshu-3600*a)//60
          c = miaoshu-3600*a-60*b
          print (a,b,c)
          continue
      ch = input('请按回车重新输入(按q退出程序):')#重新输入进入循环
      #不需要定义 ch = q 的情况，等于q将无法进入循环
