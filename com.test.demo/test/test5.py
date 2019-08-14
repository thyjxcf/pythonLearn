import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('http://python123.io/ws/demo.html')
    # print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    # print(soup.prettify()) name 属性域 attrs lxml lxml html5lib string comment
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.a)
    # print(soup.a.attrs)
    # print(soup.a.name)
    # print(soup.a.string)
    # print(soup.a.attrs['id'])
    # print(soup.a.parent.name)
    # print(soup.a.parent.parent.name)
    # print(soup.a.attrs['class'])
    # print(type(soup.a.attrs))
    # print(type(soup.a))
    # ['py1']
    # <class 'dict'>
    # <class 'bs4.element.Tag'>
    # print(soup.p.string)
    # print(soup.p)
    # print(type(soup.p.string))
    # The demo python introduces several python courses.
    # <p class="title"><b>The demo python introduces several python courses.</b></p>
    # <class 'bs4.element.NavigableString'>
    # newsoup = BeautifulSoup("<b><!--This is a comment --></b><p>This is not a comment</p>",'html.parser')
    # print(newsoup.b.string)
    # print(type(newsoup.b.string))
    # <class 'bs4.element.Comment'>

    print(soup.head)