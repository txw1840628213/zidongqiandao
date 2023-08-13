import requests
import os
import datetime
from time import sleep
import sys 
sys.path.append("..") 
import sendemail
#import pprint as p


#读取文件，提取电视台做列表
def read():
    with open("./git/tvname.txt", "r", encoding='utf-8') as f:  #打开文本
        data = f.read()   #读取文本
        tvname=data.split(",")
        #p.pprint(tvname)
        return tvname
#根据列表网页请求，错误进行保留
def re(name,t=0):
    shibai=[]
    for i in name:
        for c in range(10):
            print(i+'第'+c+'次')
            url = "http://epg.112114.xyz/?ch="+i+"&date="+data(t)
            sleep(0.5)
            requests.packages.urllib3.disable_warnings()
            # 闪出警告
        
            res = requests.get(url=url, verify=False).text
            if res.status_code == 200:
                file(i,res,t)
                break
            elif c == 9:
                shibai.append(i)
    if len(shibai) != 0:
        sendemail.send_email(0,shibai,'节目表失败')
        with open('../log.txt, 'a',encoding='utf-8') as f:
            f.write(data(t)+shibai+'\n')
            print(data(t)+"失败"+shibai)
                
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
    tvname=['CCTV1','CCTV7']#read()
    #sum=len(tvname)
    #data()
    makedir(tvname)
    re(tvname)
