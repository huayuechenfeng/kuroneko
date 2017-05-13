loglist= {}
menu = {1:"可口可乐",2:"百事可乐",3:"米饭",4:"披萨",5:"汉堡包"}
while 1 == 1 :
    dingdan = {"账号":(),"订单":[]}
    print ("欢迎使用点餐系统")
    jindu = 1
    while jindu == 1 :
        shuru1 = input("请输入您的账号\n如果没有账号，则输入zc注册\n")
        if shuru1 in loglist.keys():
                ddzh = shuru1
                jindu = 2
        elif shuru1 == "zc":
            print ("现在开始注册")
            user_zhanghao = int(input("请输入注册数字账号\n"))
            user_name = input("请输入姓名\n")
            user_tel = int(input("请输入联系方式\n"))
            print ("下面开始配置您的送餐地址")
            user_dizhi = []
            user_dizhi.append(input("请输入城市\n"))
            user_dizhi.append (input("请输入街区\n"))
            user_dizhi.append (input("请输入街道\n"))
            print ("地址配置完毕")
            nuser_xinxi ={
                "账号":user_zhanghao,
                "姓名":user_name,
                "电话":user_tel,
                "地址":user_dizhi
                }
            loglist[str(user_zhanghao)] = nuser_xinxi
            ddzh = user_zhanghao
            jindu = 2
        else:
            print ("输入错误")
    dingdan["账号"] = ddzh
    while jindu == 2:
        print ("菜单内容如下")
        for x,y in menu.items():
            print (str(x)+":"+y)
        dingdan["订单"].append(menu[int(input("请输入您要购买的商品序号（一次只能输入1个）\n"))])
        print ("您目前点了：")
        print (dingdan["订单"])
        shuru2 = input("如点餐完成，请输入a；如还需点餐，请输入此外任意值\n")
        if shuru2 == "a":
            jindu = 3
    print ("点餐完成")
    print ("以下是您的订单信息")
    print ("账号："+str(dingdan["账号"]))
    print ("点餐内容：")
    for x in dingdan["订单"]:
        print ("\t"+ x)
    print ("您的订单即将派送")
    while jindu == 3:
        shuru3 = input("关闭点餐系统，请按1\n重启点餐系统，请按2")
        if int(shuru3)== 1:
            print ("即将关闭")
            break
        elif int(shuru3)== 2:
            print ("即将重启")
            jindu = 4
        else :
            print ("输入错误")
    
    









        
        
