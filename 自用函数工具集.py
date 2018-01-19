# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:29:46 2017

@author: hasee
"""

from pandas import DataFrame
# 不可运行
# 百分数转浮点数，pandas.DataFrame必要
def per2float(lists):
    df=DataFrame({'p_str': lists})
    df2 = (df['p_str'].str.strip("%").astype(float)/100).round(decimals=2)
    flist = []
    for i in df2.index:
        values = df2.loc[i].round(decimals=2)
        print (values)
        flist.append(float(values))
    return flist

# 下载图片使用，参数：图片地址，路径，来源
def dlphoto(url,path,referer):
    kv = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    kv["referer"] = referer
    name = url.split("/")[-1]
    dlpath = path + name
    try:
        r = requests.get(url,headers = kv,timeout = 5)
        with open (dlpath,"wb") as f :
            f.write(r.content)
        print ("保存成功")  
    except:
        print ("保存失败")

# 给出名称，在指定位置创建文件夹路径，并作为返回值
def makepath(name):
    root = "d://pics//"
    path = name
    if not os.path.exists(root + path):
        os.mkdir(root + path)
    return root+path + "//"

# 输入网址，输出soup
def getHTMLsoup(url,kv="",key_ci = ""):
    try:
        kv = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        r = requests.get(url,headers=kv,params=key_ci)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser")
        return soup
    except:
        return "产生异常"
    

