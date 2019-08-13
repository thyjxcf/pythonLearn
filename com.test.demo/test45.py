import requests
from bs4 import BeautifulSoup
# soup = BeautifulSoup('<html>data</html>','html.parser')
# soup = BeautifulSoup(open('d://demo.html') ,'html.parser')

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,'html.parser')
print(soup.title)
# a标签有2个 .a只能取到第一个a标签
print(soup.a)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(soup.a.attrs)
print(soup.a.attrs['class'])
print(soup.a.attrs['href'])
print(type(soup.a))
print('------')
tag = soup.a
print(tag.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))