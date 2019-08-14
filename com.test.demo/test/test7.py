import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('http://python123.io/ws/demo.html')
    # print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    print(soup.a.next_sibling)
    print(soup.a.next_sibling.next_sibling)
    print(soup.a.previous_sibling)
    print(soup.a.previous_sibling.previous_sibling)
    print(soup.a.parent)