# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:40:09 2017

@author: hasee
"""

import requests
import bs4
from bs4 import BeautifulSoup
import os

def getHTMLsoup(url,kv="",key_ci = ""):
    try:
        kv = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        r = requests.get(url,headers=kv,params=key_ci)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser")
        return soup
    except:
        return "产生异常"
    
def geturllist(url):
    urllist = []
    r = getHTMLsoup(url)
    print (url)
    div = r.find("","MeinvTuPianBox")
    print (div)
    for ul in div.ul.find_all("","MMPic"):
        urllist.append(ul["href"])
    return urllist

def makepath(soup):
    root = "d://pics//"
    title = soup.find("h1","articleV4Tit")
    path = title.get_text()
    if not os.path.exists(root + path):
        os.mkdir(root + path)
    return root+path + "//"
def dlphoto(url,path,referer):
    kv = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    kv["referer"] = referer
    name = url.split("/")[-1]
    dlpath = path + name
    r = requests.get(url,headers = kv)
    with open (dlpath,"wb") as f :
        f.write(r.content)
        f.close()
        print ("保存成功")
    

def get_photos(url,years):
    soup = getHTMLsoup(url)
    path = makepath(soup)
    next_photo = True
    root = "http://www.27270.com/ent/rentiyishu/"+years+"//"
    while next_photo == True:
        referer = url
        data = soup.find("","articleV4Body")
        try:
            phurl = data.find("img")["src"]
            dlphoto(phurl,path,referer)
        except:
            print("无图片")
        if soup.find("li",id="nl").a["href"] != "##":
            url = root + soup.find("li",id="nl").a["href"]
            soup = getHTMLsoup(url)
        else:
            next_photo = False
            print ("本图册已经下载完毕")
root = "http://www.27270.com/ent/rentiyishu/"
url = "list_32_3.html"
7
while times < set_int:
    soup = getHTMLsoup(root + url)
    ulist = geturllist(root + url)
    for pageurl in ulist:
        years = pageurl.split("/")[-2]
        get_photos(pageurl,years)
    url = soup.find("a",text = "下一页")["herf"]
    times += 1
print ("本站爬行完毕，请检查")
    
    