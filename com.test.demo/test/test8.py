import requests
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('http://python123.io/ws/demo.html')
    # print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    # print(soup.prettify())
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # print(soup.find_all('a'))
    # print(soup.find_all(['a','b']))
    # for tag in soup.find_all(True):
    #     print(tag.name)

    # for tag in soup.find_all(re.compile('b')):
    #     print(tag)
    print(soup.find_all(id='link1'))
    print(soup.find_all('a',recursive=False))
    print(soup.find_all(string='Basic Python'))
    print(soup.find_all(string=re.compile('python')))
    pr