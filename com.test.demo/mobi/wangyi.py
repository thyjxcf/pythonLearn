import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHtmlText(url ,code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        ## 判断 网站的编码方式 而不是由程序 执行得到
        r.encoding = code

        return r.text
    except:
        return ''

def getStockList(ist,stockURL):
    html = getHtmlText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            ist.append(re.findall(r'[s][hz]\d{6}',href))
        except:
            print('')

    print('')
def getStockInfo(lst ,stockURL,fpath):
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHtmlText(url)
        try:
            if html == '':
                continue
            infoDict = []
            soup = BeautifulSoup(html ,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'classs':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all(dd)
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value
            with open(fpath , 'a' ,encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst),end=""))
        except:
            traceback.print_exc()
            print('\r当前速度：{:.2f}%'.format(count*100/len(lst),end=""))
            continue

def main():
    stock_list_url = 'http://quote.castmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'd://BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_info_url)
    getStockInfo(slist,stock_info_url,output_file)