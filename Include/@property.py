# -*- coding: utf-8 -*-
class Screen(object):
    @property#调用装饰器
    def resolution(self):#调用只读属性的resolution
        self.mianji = self._width * self._height
        return self.mianji
    @property
    def awidth(self):
        return self._width
    @awidth.setter#调用setter方法，赋值self._width
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be an integer!')
        if width < 0:
            raise ValueError('width must bigger than zero!')
        self._width = width
    @property
    def aheight(self):
        return self._height
    @aheight.setter#
    def height(self,height):#调用setter方法，赋值self._height
        if not isinstance(height,int):
            raise ValueError('height must be an integer!')
        if height < 0:
            raise ValueError('height must bigger than zero!')
        self._height = height
#测试
s = Screen()
s.width = 1024
s.height = 768
print('resolution =',s.resolution)#这里的resolution是指class中定义的函数，而s.resolution是指return的mianji
if s.resolution == 786432:
    print('测试通过！')
else:
    print('测试失败！')