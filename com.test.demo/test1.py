import requests
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# r.encoding="utf-8"
# # print(r.text)
# type(r)
kv = {'key1':'value1','key2':'value2'}
# r = requests.request('GET','http://python123.io/ws',params=kv)
r = requests.request('GET','http://python123.io/ws',json=kv)
print(r.url)
hd = {'user-agent':'Chrome/10'}
r  = requests.request('POST','http://python123.io/ws',headers=hd)

fs = {'file':open('data.xls','rb')}
r = requests.request('POST','http://python123.io/ws',files=fs)

r = requests.request('POST','http://python123.io/ws' ,timeout=10)

pxs = {'http':'http://user:pass@10.10.10.1:1234',
       'https':'http://10.10.10.1:4321'}
r = requests.request('POST','http://www.baidu.com',proxies=pxs)
