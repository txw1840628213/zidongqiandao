import requests
import json
import os
import datetime
import sendemail

#请求
def ooequ(i):
    url=os.getenv('URL')
    headers = {
    'authority': 'cdn.v2free.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '0',
    'cookie':emails[i]+keys[i],
    'origin': 'https://cdn.v2free.net',
    'referer': 'https://cdn.v2free.net/user',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
        }
    #取消证书检验
    requests.packages.urllib3.disable_warnings()
    try:
        res = requests.post(url=url,headers=headers,verify=False)
        #获取时间
        t=datetime.datetime.utcnow()
        #声明全局变量
        global s1
        s1 = (t+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S") 
        #转码
        res.encoding = 'utf-8'
        res=res.json()
    except:
        return 0
    #print(res)
    return res

#写日志
def log(n):
    f = open("log.txt", "a")
    f.write(str(s1)+" "+str(emails[i])+" "+str(n)+"\n")
    f.close()

def log_e():
    print('写入',i,emails[i] + '账号可能过期')
    f = open("log.txt", "a")
    f.write(str(s1) + " " + str(emails[i]) + " " + '签到失败' + "\n")
    f.close()
#提取响应信息
def zheng(y):
    if y['ret']==1:
        n['msg']=y['msg']
        n['剩余流量']=y['trafficInfo']['unUsedTraffic']
    elif y['ret']==0:
        n['msg']=y['msg']
    else: n['错误']='获取错误'
    return n


emails= os.getenv('USER_ID').split("\r\n")
#print(emails)
keys= os.getenv('KEY').split("\r\n")
#print(keys)

for i in range(len(emails)):
    #时间变量
    s1=None
    n={}
    h=ooequ(i)
    if h==0:
        log_e()
        text = str(s1) + "\n" + str(emails[i]) + "\n" + '签到失败' + '手动签到:\nhttps://cdn.v2free.net/user/\n\n签到日志：\nhttps://jsd.cdn.zzko.cn/gh/txw1840628213/zidongqiandao@main/log.txt'+"\n"
        sendemail.send_email(i,text,'流量签到失败')
        continue
    a=h
    n=zheng(a)
    log(n)
    print('写入',i)

