# -*- coding: UTF-8 -*-

import urllib.request
import re
import os
import urllib

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')
    
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = 'D:\\test_image'

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(path,x))
        x= x+1
    return imglist

html = getHtml("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1538009684426_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=haizeiwang")
print (getImg(html))