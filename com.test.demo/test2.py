import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() #如果不是200，产生HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text;
    except:
        return "产生异常"

#是双下划线的 并不是一个
if __name__=='__main__':
    url = "http://www.baidu.com"
    print(getHTMLText(url))


