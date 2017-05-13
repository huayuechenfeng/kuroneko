#coding=utf-8
import urllib.request
import urllib
import random
import hashlib
import http.client
import json

while True:
        #输入自己的id与密匙
	appid = 
	key = 
	salt = random.randint(1000000000,9999999999)
	fangshi =input("汉译英请按1，英译汉请按2 \n")
	if fangshi == "1" :
		fromdata = "zh"
		todata   = "en"
	else:
		fromdata = "en"
		todata   = "zh"
	neirong = str(input("请输入翻译内容\n"))
	neirong_clh = urllib.parse.quote(neirong)
	str1 = str(appid)+neirong+str(salt)+key
	md5 = hashlib.md5(str1.encode("utf8"))
	sign =md5.hexdigest()
	data = "q={0}&from={1}&to={2}&appid={3}&salt={4}&sign={5}".format(neirong_clh,fromdata,todata,str(appid),str(salt),sign)
	myurl = "/api/trans/vip/translate?"+data
	httpClient = http.client.HTTPConnection("api.fanyi.baidu.com")
	httpClient.request('GET', myurl)
	res = httpClient.getresponse()
	data_json = res.read()
	kekaku = json.loads(data_json)
	trans_result = kekaku["trans_result"]
	dicdata = trans_result[0]
	ans = dicdata["dst"]
	print (ans)
