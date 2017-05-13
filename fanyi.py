#coding=utf-8
import urllib.request
import urllib
import random
import hashlib
import http.client
import json

while True:
    #请输入您的id与密匙
    appid = 
    key = 
    salt = random.randint(1000000000,9999999999)
    jindu = 0
    while jindu == 0:
        jindu = 1
        method = input("汉译英请输入1，英译汉请输入2\n")
        if method == "1" :
            fromdata = "zh"
            todata   = "en"
        elif method == "2":
            fromdata = "en"
            todata   = "zh"
        else:
            print ("输入错误，请重新输入")
            jindu = 0
    o_text = str(input("请输入翻译内容\n"))
    o_text_clh = urllib.parse.quote(o_text)
    str1 = str(appid)+o_text+str(salt)+key
    md5 = hashlib.md5(str1.encode("utf8"))
    sign =md5.hexdigest()
    data = "q={0}&from={1}&to={2}&appid={3}&salt={4}&sign={5}".format(o_text_clh,fromdata,todata,str(appid),str(salt),sign)
    myurl = "/api/trans/vip/translate?"+data
    httpClient = http.client.HTTPConnection("api.fanyi.baidu.com")
    httpClient.request('GET', myurl)
    res = httpClient.getresponse()
    data_json = res.read()
    r_dict = json.loads(data_json)
    trans_result = r_dict["trans_result"]
    dicdata = trans_result[0]
    t_text = dicdata["dst"]
    print ("翻译结果为：")
    print (t_text)
