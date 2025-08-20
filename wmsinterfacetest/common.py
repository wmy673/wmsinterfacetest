


import requests
import json
import string,random
import uuid
server_url = 'http://82.157.138.248:8080'

def generate_random_string():
    uuid_str = str(uuid.uuid4()).replace("-", "")
    return uuid_str

def t1est_01():
    url = 'http://82.157.138.248:8080/jeewms/rest/pdaapi/login'
    body = {"userName":"admin", "password":"llg123"}

    r = requests.post(url, json=body,timeout=10).json()
    print("查看响应：", r)

def t1est_02():
    url = server_url + '/jeewms/rest/pdaapi/mdGoodsController/list'
    body = {"username":"", "searchstr":""}
    r = requests.get(url, json=body, timeout=10).json()

    print("商品列表接口：", json.dumps(r, indent=4, ensure_ascii=False))

def t1est_03():
    url = 'http://82.157.138.248:8080/jeewms/mdGoodsController.do?doAdd'
    headers = {"Cookie": "JJEECGINDEXSTYLE=ace; ZINDEXNUMBER=1990; JSESSIONID=4CF542C5E0E7C0C375F9FDE01F7E6ED6"}
    # headers = {"Content-Type": "application/x-www-form-urlencoded"} ,
    #         "Content-Type": "application/x-www-form-urlencoded"
    body = {
        "id": "",
        "updateBy": "admin",
        "suoShuKeHu": "X00001",
        "cfWenCeng": "冷藏",
        "chpShuXing": "日用",
        "gaoDanPin": "1000",
        "shpBianMa": "LV013",
        "shpMingCheng": "奢侈全身3",
        "shlDanWei": "个",
        "chlKongZhi": "N",
    }
    bodystr = json.dumps(body, ensure_ascii=False)
    print(bodystr)

    data = {"mdGoodsstr":bodystr}
    r = requests.post(url, data=body,headers=headers, timeout=10).json()
    print("查看响应：", r)


def t1est_04():
    url = 'http://82.157.138.248:8080/jeewms/loginController.do?login'
    r = requests.get(url).cookies
    print(r)
    print(r.get('JSESSIONID'))

def test_05():
    url = 'http://82.157.138.248:8080/jeewms/loginController.do?checkuser'
    headers = {"content-type":"application/x-www-form-urlencoded", "cookie":"JEECGINDEXSTYLE=ace; ZINDEXNUMBER=2030; JSESSIONID=DA3C8569C0C7F6D4F4BC706D85468C07"}
    body = {"userName":"admin","password":"llg123","randCode":"7772","langCode":"zh-cn"}
    r = requests.post(url,data=body).json()
    print(r)


import base64
if __name__ == '__main__':
    # token_base64 = base64.b64encode("管理员".encode('utf-8')).decode('utf-8')
    # print(token_base64)
    # token_base65 = base64.b64encode("管理员".encode('utf-8')).decode('ascii')
    # print(token_base65)
    # test_03()
    test_05()

