
import urlconfig
import requests


class TestLogin():

    # 正面用例
    def test_01(self):
        url = urlconfig.server_url + urlconfig.login_url
        body = {
            "userName": "admin",
            "password": "llg123",
        }
        # data, json, params
        r = requests.post(url, json=body, timeout=5)

        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", r)
        assert r.get('code') == 200
        assert r.get('result').get('userKey') == '管理员'

    # 错误密码
    def test_02(self):
        url = urlconfig.server_url + urlconfig.login_url
        body = {
            "userName": "admin",
            "password": "llg12",
        }
        # data, json, params
        r = requests.post(url, json=body, timeout=5)
        print("看看未转json时的响应体：", r)
        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", r)
        assert r.get('code') == 500
        assert r.get('message') == '获取TOKEN,账号密码错误!'

    # 账号不存在
    def test_03(self):
        url = urlconfig.server_url + urlconfig.login_url
        body = {
            "userName": "admin1",
            "password": "llg123",
        }
        # data, json, params
        r = requests.post(url, json=body, timeout=5)
        print("看看未转json时的响应体：", r)
        assert 200 == r.status_code
        r = r.json()
        print("整个响应体的json格式内容：", r)
        assert r.get('code') == 500
        assert r.get('message') == '获取TOKEN,账号密码错误!'