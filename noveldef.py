#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 22:30:58 2018
@author: shukebeita
"""

import requests
from lxml import etree
import time
import os
import sys

baseurl = 'https://www.biqubao.com'

headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400"
}
#书名
def get_title(id):
    bookid = str(id)
    url = baseurl + '/book/' + bookid
    r = requests.get(url,headers)
    r.encoding="gbk"
    html = r.text
    s = etree.HTML(html)
    title = s.xpath('//*[@id="info"]/h1/text()')
    return title[0]

#章节链接 （ list ）
def get_linklist(id):
    bookid = str(id)
    url = baseurl + '/book/' + bookid
    r = requests.get(url,headers)
    r.encoding="gbk"
    html = r.text
    s = etree.HTML(html)
    links = s.xpath('//*[@id="list"]/dl/dd/a/@href')
    return links

#章节名称 + 正文
def get_text(link):
    url = baseurl + link
    r = requests.get(url,headers)
    r.encoding="gbk"
    html = r.text
    fulltext = ''
    s = etree.HTML(html)
    chaptername1 = s.xpath('//div[@class="bookname"]/h1/text()')
    if len(chaptername1) > 0:
        chaptername = chaptername1[0]
    else:
        chaptername = ''
    print(chaptername)
    fulltext = fulltext + '\n' + chaptername + '\n\n'
    texts = s.xpath('//*[@id="content"]/text()')
    for text in texts:
        fulltext = fulltext + text.strip()
    fulltext = fulltext + '\n'
    return fulltext

def get_ebook(id):
    links = get_linklist(id)
    cps = len(links)
    bookname = get_title(id)
    print(bookname,'章节总数:',cps)
    startchapter=int(input('输入起始章节\n'))
    basedir = 'novels/' + bookname + '.txt'
    with open(basedir,'w+',encoding = 'utf-8') as f:
        f.write('\n' + bookname + '\n')
        f.close()
    for i in range(startchapter-1,cps):
        with open(basedir,'a+',encoding = 'utf-8') as f:
            f.write(get_text(links[i]))
            f.close()
        print('\t\t\t\t\t','(',i+1,'of',cps,')')
        time.sleep(1)
    href = "<a href='novels/" + bookname + ".txt' target='_blank'>" + bookname + "</a><br>"
    print()
    print('将下载内容添加到网页链接')
    print()
    with open('novellist.html','a+',encoding = 'utf-8') as f:
        f.write('\n' + href + '\n')
        f.close()

id=input('下载请输入书籍编号,提交代码码请直接按Enter键,按Q键退出\n')
if id=='q' or id=='Q': 
    print('程序退出')
    sys.exit()

if id!='':
    get_ebook(id)
    print('提交到git远程仓库')
    os.system('git add -A')
    os.system("git commit -m '下载完成,自动提交'")
    os.system('git push')

if id=='':
    print('提交代码到远程仓库')
    os.system('git add -A')
    comm = input('提交注释内容:(暂不支持中文内容)\n')
    if comm == '':
        comm = '自动提交代码到远程仓库'
    comm = "git commit -m '" + comm + "'"
    os.system(comm)
    os.system('git push')

