import requestsimport osimport reimport bs4import tracebackfrom bs4 import BeautifulSoupdef getHtmlText1(url):    try:        hd = {'user-agent':'Chrome/10'}        r = requests.request('GET',url,headers=hd)                r.raise_for_status()        r.encoding = 'utf-8'        # print(r.text)        # print(r.status_code + "  dddddddd ")        return r.text    except:        traceback.print_exc()        return ''def parseHtml(list ,html):    try:        soup = BeautifulSoup(html,'html.parser')        # answer = soup.find_all('div' ,attrs={'data-type':'Answer'});        for div in soup.find_all('div' ,attrs={'data-type':'Answer'}):        # for i in range(1):        #     div = answer[i]            h2 = div.find('a').string;            print(h2 + '\n')            h2Str = '<h2>' + h2 + '</h2>'            answerDiv = div.find('div',attrs={'data-action':'/answer/content'})            # print(type(answerDiv))            # print(answerDiv)            content = answerDiv.find('textarea',attrs={'class':'content'})            # print(content.contents)            str1 = ''            for p in BeautifulSoup(content.contents[0] ,'html.parser').find_all('p'):                if isinstance(p,bs4.element.Tag):                    if p.string is None:                        str1 = str1 + '</br>'                    else:                        str1 = str1 + str(p.string) + '</br>'            str1 = str1 + '<br>'            print(str1)            list.append([h2Str,str1])        print(len(list))    except:        traceback.print_exc()def download(list):    root = 'C:\E\pic/'    path = root +'2.txt'    try:        if not os.path.exists(root):            os.mkdir(root)        if  not os.path.exists(path):            with open(path,'a'  ,encoding='utf-8') as f:                f.write('<html lang="en"><head><meta charset="UTF-8"><title>赞同超过1000的回答2</title></head><body>')                f.write('<h1>赞同超过1000的回答2</h1>')                f.close();        with open(path,'a'  ,encoding='utf-8') as f:            for l in list:                f.write(l[0] + '</br>')                f.write(l[1] + '</br>')                print('文件保存成功')            f.write('</body></html>')            f.close();    except:        traceback.print_exc()def forIterator(ind):    for index in range(ind):        page = index + 100        ilist=[]        url = 'https://www.zhihu.com/collection/19928423?page='+str(page)        html = getHtmlText1(url)        parseHtml(ilist,html)        download(ilist)if  __name__== '__main__':    # ilist=[]    # html = getHtmlText1('https://www.zhihu.com/collection/19928423?page=1')    # parseHtml(ilist,html)    # download(ilist)    forIterator(15)