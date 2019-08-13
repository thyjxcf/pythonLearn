import requests
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# r.encoding="utf-8"
# # print(r.text)
# type(r)
kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)
