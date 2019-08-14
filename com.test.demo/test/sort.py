import requests
from bs4 import BeautifulSoup
import bs4
def getHtml(url):

    try:
        r = requests.get('http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo,'html.parser')
        for tag in soup.find('tbody').children:
            if isinstance(tag,bs4.element.Tag):
                    tds = tag.find_all('td')

                    print(tds[0] + '   ' + tds[1] + '    ' + tds[3])



    except:
        # print
        print('解析错误')



if __name__ == '__main__':
    url ='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    getHtml(url)
