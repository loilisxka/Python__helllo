# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def getstockhtml(url, code='utf-8'):#获取网页信息的函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code#直接通过认为检查header，进行赋值，降低系统的工作复杂度
        return r.text
    except:
        return ''

def getstocklist(list, url):#获取所有股票列表
    html = getstockhtml(url)
    soup = BeautifulSoup(html, 'html.parser')#做汤
    a = soup.find_all('a')#寻找所有a的标签
    for i in a:
        try:
            href = i.attrs['href']#提取标签中的href属性
            list.append(re.findall(r'[s][zh]\d{6}', href)[0])#匹配语句中的股票代码
        except:
            continue

def printstockinfo(list, url1, path):
    count = 0
    for i in list:#改变前缀，符合网易股票代码的规则
        if 'sh' in i:
            i = '0' + i[2:]
        else:
            i = '1' + i[2:]
        url = url1 + i + '.html'#创立新的url链接
        html = getstockhtml(url)
        try:
            if html == '':
                continue
            soup = BeautifulSoup(html, 'html.parser')#做汤
            info = soup.find('div', attrs={'class': 'relate_stock clearfix'})#寻找div标签，并且该标签中有class属性
            stock = info.find_all('script')[0]#取出我们需要的股票信息
            with open(path, 'a', encoding='utf-8') as f:#打开文件，进行读写操作
                f.write(str(stock.string) + '\n')
                count += 1
                print('\r当前进度:{:0.2f}%'.format(count*100/len(list)), end='')#显示进度
        except:
            count += 1
            print('\r当前进度:{:0.2f}%'.format(count * 100 / len(list)), end='')
            continue

def main():
    get_stock_list = 'http://quote.eastmoney.com/stocklist.html'
    get_stock_price = 'http://quotes.money.163.com/'
    path = 'C://360//stock.txt'
    info = []
    getstocklist(info, get_stock_list)
    printstockinfo(info, get_stock_price, path)

main()