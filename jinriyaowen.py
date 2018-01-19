# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:14:40 2017

@author: hasee
"""
import requests
import bs4
from bs4 import BeautifulSoup
def getHTMLsoup(url,kv="",key_ci = ""):
    try:
        r = requests.get(url,headers=kv,params=key_ci)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser")
        return soup
    except:
        return "产生异常"
    
if __name__ == "__main__":
    url = "http://news.sina.com.cn"
    #kv = {"user-agent":"Mozilla/6.0"}
    soup = getHTMLsoup(url)
    news = soup.find(id="blk_yw_01")
    print (news.find("","b_time").string)
    yaowen = news.find(id="syncad_1")
    for newss in yaowen.find_all("a"):
        print (newss.string)
    r = input()
    print(r)
        
