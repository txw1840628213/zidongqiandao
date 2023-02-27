import requests
import json
import os
import datetime
#请求
def ooequ(i):
    url=os.getenv('URL')
    headers={
        'accept':'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-length': '0',
        'cookie':emails[i]+keys[i]
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
        print(email[i]+'账号可能过期')
        f = open("log.txt", "a")
        f.write(str(s1)+" "+str(emails[i])+" "+'签到失败'+"\n")
        f.close()
    #print(res)
    return res

#写日志
def log(n):
    f = open("log.txt", "a")
    f.write(str(s1)+" "+str(emails[i])+" "+str(n)+"\n")
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
print(emails)
keys= os.getenv('KEY').split("\r\n")
print(keys)

for i in range(len(emails)):
    #时间变量
    s1=None
    n={}
    a=ooequ(i)
    n=zheng(a)
    log(n)
    print('写入',i+1)

