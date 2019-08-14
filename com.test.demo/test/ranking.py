import requests
from bs4 import BeautifulSoup
import bs4
def getHtmlText(url):
    try:
        r = requests.get(url ,timeout=30)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ''


    return  ""


def fillUnivList(uList , html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        # 检查tr的类型
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string,tds[1].string,tds[3].string])

    pass

def printUnivList(uList,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","大学名称","总分"))
    for i in range(num):
        u = uList[i]
        print(tplt.format(u[0],u[1],u[2]))
    print("Suc" + str(num))

# 主函数
def  main():
    uinfo = []
    url ='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  # 只列出20所

if __name__ == '__main__':
    main();


