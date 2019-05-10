#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 22:30:58 2018
@author: shukebeita
"""

import os


os.system('git add -A')
comm = input('提交注释内容(输入完成后请切换到英文输入):\n')
if comm == '':
    comm = '自动提交代码到远程仓库'
    comm = "git commit -m '" + comm + "'"
    os.system(comm)
    os.system('git push')
if comm != '':
    comm = "git commit -m '" + comm + "'"
    os.system(comm)
    os.system('git push')
print('更新完成')
