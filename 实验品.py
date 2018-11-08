# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def findunpai(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '1'

def fillun(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printun(ulist, num):
    print('{:^10}\t{:^10}\t{:^10}'.format('排名', '大学', '总分'))
    for i in range(num):
        u = ulist[i]
        print('{:^10}\t{:^10}\t{:^10}'.format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html = findunpai(url)
    fillun(html, uinfo)
    printun(uinfo, 20)
main()