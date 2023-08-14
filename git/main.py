import requests
import os
import datetime
from time import sleep 
import sendemail
#import pprint as p


#读取文件，提取电视台做列表
def read():
    with open("./git/tvname.txt", "r", encoding='utf-8') as f:  #打开文本
        data = f.read()   #读取文本
        data = data[:-1]
        tvname=data.split(",")
        #p.pprint(tvname)
        return tvname
#根据列表网页请求，错误进行保留
def re(name,t=0):
    shibai=[]
    headers = {
    'authority': 'epg.112114.eu.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
}
    for i in name:
        for c in range(10):
            print(i+'第',c,'次')
            url = "http://epg.112114.eu.org/?ch="+i+"&date="+data(t)
            
            requests.packages.urllib3.disable_warnings()
            # 闪出警告
        
            res = requests.get(url=url,headers=headers verify=False)
            sleep(1)
            print(res.status_code)
            if res.status_code == 200 || res.status_code == 201:
                file(i,res.text,t)
                break
            elif c == 9:
                shibai.append(i)
    if len(shibai) != 0:
        sendemail.send_email(0,str(shibai),'节目表失败')
        with open('./log.txt', 'a',encoding='utf-8') as f:
            f.write(data(t)+str(shibai)+'\n')
            print(data(t),"失败",shibai)
                
    return res
#命名，写入文件
def file(i,res,t=0):
    with open('./list/'+i+'/'+data(t), 'w',encoding='utf-8') as f:
        f.write(res+'\n')
        print(data(t)+"写入"+i)


#创建文件夹
def makedir(tvname):
    for i in tvname:
        path = "./list/" + i
        #判断文件夹是否存在
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)


    #时间
def data(t=0):

    #datetime.datetime.now() 现在时间 ，datetime.timedelta(days=) 加（减负）天数 ， .strftime("%Y-%m-%d") 格式
    time=(datetime.datetime.utcnow()+datetime.timedelta(hours=8)+datetime.timedelta(days=t)).strftime("%Y-%m-%d")
    return time
if __name__ == '__main__':
    tvname=read()
    #sum=len(tvname)
    #data()
    makedir(tvname)
    re(tvname)
