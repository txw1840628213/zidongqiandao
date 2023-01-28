import requests
import json

from datetime import datetime
def ooequ(i):
    url='https://cdn.v2free.net/user/checkin'

    headers={
        'accept':'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-length': '0',
        'cookie':emails[i]+keys[i]
        }
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=url,headers=headers,verify=False)
    t=datetime.now()
    global s1
    s1 = t.strftime("%Y-%m-%d %H:%M:%S") 
    res.encoding = 'utf-8'
    res=res.json()
    '''    print(res.status_code)
    res=res.json()
   
    print(emails[i]+res['msg'])
    '''
    
    return res
def log(n):
    f = open("log.txt", "a")
    f.write(str(s1)+" "+str(emails[i])+" "+str(n)+"\n")
    f.close()
def zheng(y):
    if y['ret']==1:
        n['msg']=y['msg']
        n['剩余流量']=y['trafficInfo']['unUsedTraffic']
    elif y['ret']==0:
        n['msg']=y['msg']
    else: n['错误']='获取错误'
    return n

emails=['uid=113435;email=4dung9d3um%40klovenode.com;',
        'uid=112215;email=826696974%40qq.com;',
        'uid=58797; email=wxt1.1@qq.com;'
        ]
keys=['key=ab3c13dc4a552e8e5304fc4e6e83fdf199232c57fc714;expire_in=1677340228',
      'key=36119318cfba49902fa0955c2f46738f2792d1cf369bf;expire_in=1677483902',
      'key=b58d5e4cb907e94b9e44218a32cd3f02482b16bc2e17a;expire_in=1677494148']


for i in range(len(emails)):
    s1=None
    n={}
    a=ooequ(i)
    n=zheng(a)
    log(n)
    print('写入',i+1)

