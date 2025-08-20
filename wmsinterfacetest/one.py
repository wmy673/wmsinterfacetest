import requests
import base64
import json
import sys
import random

# 配置服务器地址信息
SERVER_URL = "http://82.157.138.248:8080/jeewms/rest/pdaapi"
USERNAME = "admin"
PASSWORD = "llg123"

# 全局变量存储测试数据
test_data = {
    "token": None,
    "product_record": None
}


# 获取登录认证Token
def get_auth_token():
    url = f"{SERVER_URL}/login"
    payload = {"userName": USERNAME, "password": PASSWORD}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        # wms登陆验证方式是通过token，所以用全局变量传递给后面的测试用例
        token = response.json()["result"]["userKey"]
        token_base64 = base64.b64encode(token.encode('utf-8')).decode('ascii')
        test_data["token"] = token_base64

        return token_base64

    except Exception:
        return None


# 获取认证请求头
def get_auth_headers(token_base64):
    return {
        "Authorization": f"Bearer {token_base64}",
        "Content-Type": "application/json"
    }


# 测试商品列表接口
def product_list(token_base64):
    url = f"{SERVER_URL}/mdGoodsController/list"
    headers = get_auth_headers(token_base64)
    params = {"username": USERNAME}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)

        data = response.json()
        data_field = "obj" if "obj" in data else "data"
        records = data.get(data_field, [])
        test_data["product_record"] = records[-1]

        return True

    except Exception:
        return False


# 测试商品提交接口
def submit_product(token_base64):
    product_record = test_data["product_record"]
    url = f"{SERVER_URL}/mdGoodsController/save"
    headers = get_auth_headers(token_base64)

    # 构造商品数据
    payload = {
        "id": product_record.get("id"),
        "updateBy": USERNAME,
        "suoShuKeHu": product_record.get("suoShuKeHu", "X00001"),
        # "shpMingCheng": product_record.get("shpMingCheng", "商品") + " (更新aaa)",
        "shpMingCheng": "牛羊肉aasd呼哈",
        # "shpBianMa": product_record.get("shpBianMa", f"CODE{random.randint(1000, 9999)}"),
        # "bzhiQi": str(int(product_record.get("bzhiQi", 180)) + random.randint(1, 30)),
        # "tiJiCm": str(int(product_record.get("tiJiCm", "5000")) + random.randint(100, 500)),
        # "zhlKg": str(float(product_record.get("zhlKg", "25")) + random.uniform(0.1, 5.0)),
        # "chZhXiang": str(int(product_record.get("chZhXiang", "50")) + random.randint(1, 10)),
        # "kuZhXiang": str(int(product_record.get("kuZhXiang", "40")) + random.randint(1, 10)),
        # "gaoZhXiang": str(int(product_record.get("gaoZhXiang", "30")) + random.randint(1, 10))
    }

    # 将payload转换为JSON字符串
    json_str = json.dumps(payload, ensure_ascii=False)

    # 构造表单数据
    data = {"mdGoodsstr": json_str}

    # 修改请求头为表单格式
    form_headers = headers.copy()
    form_headers["Content-Type"] = "application/x-www-form-urlencoded"

    try:
        response = requests.post(url, data=data, headers=form_headers, timeout=15)
        data = response.json()
        print(data)
        return True
    except Exception:
        return False


def run_tests():
    """执行所有API测试"""
    token_base64 = get_auth_token()
    if not token_base64:
        print("登录失败")
        return

    # 执行测试用例
    tests = [
        ("商品列表", product_list, token_base64),
        ("商品提交", submit_product, token_base64)
    ]

    results = []
    for name, test_func, arg in tests:
        success = test_func(arg)
        results.append((name, success))
        print(f"{name}接口: {'✅ 成功' if success else '❌ 失败'}")

    # 打印测试摘要
    success_count = sum(1 for _, success in results if success)
    total = len(results)
    print(f"\n测试完成! 成功率: {success_count}/{total}")

run_tests()