import requests
import json
from bs4 import BeautifulSoup
# soup = BeautifulSoup('<html>data</html>','html.parser')
# soup = BeautifulSoup(open('d://demo.html') ,'html.parser')
# http://test.approute.kai12.cn:8060/authorization/oauth2/access_token?
# grant_type=authorization_code&client_id=Wfl9GTllE8ETMAeTW5YDS2VlHKFBY5ck&client_secret=oh267xUne2Bsal3PzkV2P1H8q8YIIYQ9&code=f55610077457ba18c86c0394581577fc


if __name__ == '__main__':
    kv={'grant_type':'authorization_code','client_id':'Wfl9GTllE8ETMAeTW5YDS2VlHKFBY5ck','client_secret':'oh267xUne2Bsal3PzkV2P1H8q8YIIYQ9','code':'748232b208c91818d051fdb3c78d1441'}
    r = requests.post('http://183.250.187.102:808/authorization/oauth2/access_token',data=kv)
    data = r.text;
    json_data = json.loads(data)
    open_id = json_data['openid']
    access_token = json_data['access_token']
    kv = {'open_id':open_id}
    hd = {'Authorization':access_token}
    r = requests.get('http://183.250.187.102:808/common/get_user_info',params=kv ,headers=hd)
    print(r.text)
