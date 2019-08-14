import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('http://python123.io/ws/demo.html')
    # print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    # print(soup.head)
    #     # print(soup.head.contents)
    #     # print(soup.body.contents)
    #     # print(len(soup.body.contents))
    #     # print(soup.body.contents[1])
    # print(soup.title.parent)
    # print(soup.html.parent)
    # print(soup)
    # soup = BeautifulSoup(demo,'html.parser')
    # for parent in soup.a.parents:
    #     if parent is None:
    #         print(parent)
    #     else:
    #         print(parent.name)

        #     p
        # body
        # html
        # [document]