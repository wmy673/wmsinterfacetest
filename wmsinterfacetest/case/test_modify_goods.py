
import urlconfig
import requests
import random,json


class TestModifyGoods():

    # 正面用例-修改全部必填项地址
    def t1est_01(self,getheaders):

        # 添加商品的接口
        url = urlconfig.server_url + urlconfig.goodssavemodify_url

        n = random.randint(10, 100)
        bianma = "LV031" + str(n)
        body = {
            "id": "ff8080819823849b01984053d59602b5",
            "updateBy": "admin",
            "suoShuKeHu": "X00001",
            "cfWenCeng": "常温",
            "chpShuXing": "日用",
            "gaoDanPin": "1000",
            "shpBianMa": bianma,
            "shlDanWei": "份",
            "chlKongZhi": "Y",
        }

        # 把字典转化成json字符串
        bodystr = json.dumps(body, ensure_ascii=False)

        # 构建请求体
        data = {"mdGoodsstr": bodystr}

        # data, json, params
        r = requests.post(url, data=data, headers=getheaders, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", r)
        assert True == r.get('ok')

    # 正面用例-修改商品名
    def test_02(self, databascursor):
        # 添加商品的接口
        url = urlconfig.server_url + urlconfig.goodssavemodify_url

        headers = {
            "Authorization": f"Bearer 566h55CG5ZGY",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

        n = random.randint(10, 100)
        bianma = "LV031" + str(n)
        body = {
            "id": "ff8080819823849b01984053d59602b5",
            "shpMingCheng": "自动化接口测试用到的数据，勿动！！",
        }

        # 把字典转化成json字符串
        bodystr = json.dumps(body, ensure_ascii=False)

        # 构建请求体
        data = {"mdGoodsstr": bodystr}

        # data, json, params
        r = requests.post(url, data=data,headers=headers, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", r)
        assert True == r.get('ok')
        databascursor.execute('select shp_ming_cheng where id = "ff8080819823849b01984053d59602b5"')
        print(databascursor.fetchall())

