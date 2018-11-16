# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getedhtml(url, code='utf-8'):
    kv = {'user-agent': 'Mozilla/5.0'}#网站有反爬虫措施，需要改变headers，来伪装自己
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''

def returned(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody', 'hidden_zhpm').children:#寻找其中的tbody标签
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            list.append([tds[0].contents[0], tds[1].string, tds[3].string])
    #这里的tds[0]实际是一个包含了很多节点的父亲节点，所以取出其中的第一项就是我们需要的排名

def printlist(list, num):
    print('{:^10}{:^10}{:^10}'.format('排名', '大学', '分数'))
    for i in range(num):
        L = list[i]
        print('{:^10}{:^10}{:^10}'.format(L[0], L[1], L[2]))

def main():
    L = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    num = int(input('您要查找前几名的大学：'))
    html = getedhtml(url)
    returned(html, L)
    printlist(L, num)

main()