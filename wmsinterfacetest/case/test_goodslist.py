
import urlconfig
import requests
import json


class TestGoodsList():

    # username必填项未填写
    def test_01(self):
        url = urlconfig.server_url + urlconfig.goodslist_url
        body = {
           "username": "",
            "searchstr": "RL001"
        }
        # data, json, params
        r = requests.get(url, json=body, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", json.dumps(r, indent=4, ensure_ascii=False))

        assert r.get('ok') == False

    # 商品编码参数searchstr填写内容
    def test_02(self):
        url = urlconfig.server_url + urlconfig.goodslist_url
        body = {
            "username": "管理员",
            "searchstr": "RL001"
        }
        # data, json, params
        r = requests.get(url, json=body, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", json.dumps(r, indent=4, ensure_ascii=False))
        assert len(r.get('obj')) <= 1
        assert r.get('obj')[0].get('shpBianMa') == 'RL001'

    # 只有必填项参数username,且系统没有对应的数据记录
    def test_03(self):
        url = urlconfig.server_url + urlconfig.goodslist_url
        body = {
            "username": "AAXXSS",
        }
        # data, json, params
        r = requests.get(url, json=body, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", json.dumps(r, indent=4, ensure_ascii=False))
        assert len(r.get('obj')) == 0


