



import pytest
import requests
import urlconfig
import base64, pymysql


@pytest.fixture(scope='session')
def getheaders():
    url = urlconfig.server_url + urlconfig.login_url
    body = {
        "userName": "admin",
        "password": "llg123"
    }
    r = requests.post(url, json=body, timeout=5).json()
    userkey = r.get('result').get('userKey')
    token = base64.b64encode(userkey.encode('utf-8')).decode('ascii')
    print("token值的样式：", token)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    yield headers

@pytest.fixture(scope='session')
def databascursor():
    con = pymysql.connect(host='82.157.138.248', user='root', password='123456aA', database='wms')
    cursor = con.cursor()
    yield cursor
    cursor.close()
    con.close()



