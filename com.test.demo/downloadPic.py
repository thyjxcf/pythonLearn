import requests
import os

def downloadPic(url):
    root = 'd://pics/'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')

    except:
        print('爬取失败')

if __name__ == '__main__':
    url='http://img0.dili360.com/ga/M00/49/B7/wKgBzFqo8g6ACnjtAAYuBBnO5p0219.tub.jpg@!rw17'
    downloadPic(url)
