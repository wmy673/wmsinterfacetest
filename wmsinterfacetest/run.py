

import pytest
import os

if __name__ == '__main__':
    # --alluredir  指定目录用于存放生成的中间数据
    # --clean - alluredir  每次执行项目前，先清空目录下的内容
    pytest.main(['./case/test_modify_goods.py', '-s', '--alluredir', './temp', '--clean-alluredir'])
    # os.system(f'allure generate temp -o allure-report --clean')  # 这种方式可以生成html文件
