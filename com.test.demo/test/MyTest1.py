import requests

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()

        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print('解析错误')


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # getHtml(url)
    kv = {'k1':'v1','k2':'v2'}
    r = requests.post(url,params=kv)
    print(r.url)


