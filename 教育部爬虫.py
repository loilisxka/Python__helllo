# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getedhtml(url, code='utf-8'):
    kv = {'user-agent': 'Mozilla/5.0'}#网站有反爬虫措施，需要改变headers，来伪装自己
    try:
        r = requests.get(url, headers=kv, timeout=30)#改变自己的headers变量
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''

def returned(html):
    soup = BeautifulSoup(html, 'html.parser')#做汤
    div = soup.find_all('div', 'TRS_Editor')[2].children#寻找第三个拥有该属性的节点，并创建可遍历的迭代器
    for li in div:#遍历该迭代器，虽然其中只有一个儿子节点（需要想办法解决）
        if isinstance(li, bs4.element.Tag):
            ul = li.find_all('span')#寻找所有span节点
            a = li.find_all('a')#寻找所有a节点
            for i in range(len(ul)):#按顺序进行输出
                print(str(ul[i].string))
                print(str(a[i].string))

def main():
    url = 'http://www.moe.gov.cn/'
    html = getedhtml(url)
    returned(html)

main()