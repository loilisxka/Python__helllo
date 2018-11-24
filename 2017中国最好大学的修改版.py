# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getedhtml(url, code='utf-8'):
    kv = {'user-agent': 'Mozilla/5.0'}#网站有反爬虫措施，需要改变headers，来伪装自己
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r. raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''

def returned(html, list, num):
    count = 0                                           #对加入列表中的信息进行计数
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find('tbody', 'hidden_zhpm').children
    for tr in info:
        if count >= num:
            break                                       #如果以及满足所需要的高校数，就可以退出了
        if isinstance(tr, bs4.element.Tag):
            count += 1
            tds = tr.find_all('td')
            list.append([tds[0].contents[0], tds[1].string, tds[3].string])

def printed(list, num):
    print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format('排名', '高校', '分数', chr(12288)))
    for i in range(num):
        L = list[i]
        print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format(L[0], L[1], L[2], chr(12288)))


def main():
    list = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    num = int(input('请问要查询2017前多少名的高校呢：'))
    html = getedhtml(url)
    returned(html, list, num)
    printed(list, num)

main()