# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from urllib import request
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_title = False#设置标志旗子，方便程序寻找有效字符段
        self.is_location = False
        self.is_time = False
        self.times = []#用来存放我们抓取的临时数据
        self.event = {}
        self.eventList = []
    def handle_starttag(self,tag,attrs):#确定哪些字符段是有效字符段
        if ('class','event-location')in attrs:
            self.is_location = True
        if ('class','event-title') in attrs:
            self.is_title = True
        if tag == 'time':
            self.is_time = True
    def handle_endtag(self,tag):#确定抓取动作到哪里结束
        if tag == 'span':
            self.is_location = False
        if tag == 'h3':
            self.is_title = False
        if tag == 'time':
            self.event['time'] = ''.join(self.times)
            self.is_time = False#重置旗子和列表
            self.times = []
        if tag == 'li' and self.event:
            self.eventList.append(self.event)#把一个小会议加入所有会议的列表中
            self.event = {}#重置列表
    def handle_data(self,data):#把抓取出来的语句，以字典的形式放进去
        if self.is_title:
            self.event['title'] =data
        if self.is_location:
            self.event['location'] = data
        if self.is_time:
            self.times.append(data)
    def showEvent(self):#打印我们爬取的数据
        for event in self.eventList:
            print('title:',event['title'])
            print('location:',event['location'])
            print('time:',event['time'])
            print('-----------------------------')
with request.urlopen('https://www.python.org/events/python-events/') as f:#打开需要爬取的页面
    data = f.read()
parser = MyHTMLParser()#赋予实例
parser.feed(data.decode('utf-8'))
parser.showEvent()#打印


