


import requests


def addgoods():
    url = 'http://82.157.138.248:8080/jeewms/mdGoodsController.do?doAdd'
    headers= {"content-type":"application/x-www-form-urlencoded; charset=UTF-8", "cookie":"JEECGINDEXSTYLE=ace; JSESSIONID=C813058FAB1E4AB59603E7F23AF55BA1; ZINDEXNUMBER=2020"}  # ; ZINDEXNUMBER=2020 "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    body = {"suoShuKeHu":"X00001", "cfWenCeng":"冷藏", "chpShuXing": "日用", "gaoDanPin":"109", "shpBianMa":"LV024", "shpMingCheng": "衬衫", "shlDanWei":"件", "chlKongZhi":"N"}
    r = requests.post(url, headers=headers, data=body,timeout=10).json()
    print(r)

import json
def goodslist():
    url = 'http://82.157.138.248:8080/jeewms/rest/pdaapi/mdGoodsController/list'
    r = requests.get(url).json()
    print("查看商品列表得到的数据：", json.dumps(r,indent=4, ensure_ascii=False))

def getauthtoken():
    import base64
    token = base64.b64encode("管理员".encode('utf-8')).decode('ascii')
    print(token)

def addgoodsinterface():
    url = 'http://82.157.138.248:8080/jeewms/rest/pdaapi/mdGoodsController/save'
    headers = {
        "Authorization": f"Bearer 566h55CG5ZGY",
        "Content-Type": "application/json"
    }
    body = {
        "id": "ff8080819823849b01983821c8b20190",
        "updateBy": "admin",
        "suoShuKeHu": "X00001",
        "cfWenCeng": "冷藏",
        "chpShuXing": "日用",
        "gaoDanPin": "1000",
        "shpBianMa": "LV031",
        "shpMingCheng": "正课",
        "shlDanWei": "个",
        "chlKongZhi": "N",
    }
    jsonstr = json.dumps(body, ensure_ascii=False)
    body = {"mdGoodsstr": jsonstr}


    r = requests.post(url, headers=headers,params=body,timeout=10).json()
    print("修改后的商品信息：", r)

addgoodsinterface()

