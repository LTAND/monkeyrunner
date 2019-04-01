#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

path1 = os.path.abspath(".")  # os.getcwd() 当前路径
path3 = os.path.abspath("/")
path2 = os.path.abspath("..")  
hello = os.popen(str(path1)+'/hello/hello.py').read() 
helloMine = os.popen('helloMine.py').read() 

print('当前路径.：',path1,'\n上一级路径/',path2, '\n磁盘路径：',path3)
print('hello:',hello)
print('helloMine:',helloMine)


