import requests

r = requests.get('https://item.jd.com/100000287115.html')
print(r.status_code)
print(r.encoding)
print(r.text)