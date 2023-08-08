from urllib.parse import urljoin
import re
import time
import pytest
import requests
from common.yaml_util import YamlUtil


# Authorization = "Basic c2FiZXI6c2FiZXJfc2VjcmV0"

# 一般写在conftest.py里，不需要导入
# @pytest.fixture(scope="function")
# def connect_database():
#     print("连接数据库")
#     yield
#     print("关闭数据库")# yield，在引用该修饰器函数执行完毕之后，执行yield后面的内容
#     #yield作为一个生成器，相当于返回一个对象


def test_outclass():
    # time.sleep(3)
    print("类外测试函数")

def test_rerun():
    assert 1==1

class TestLogin:

    def setup(self):
        print("每个用例之前执行一次")

    def setup_class(self):
        print("测试类开始时执行一次")

    def teardown(self):
        print("每个用例之后执行一次")

    def teardown_class(self):
        print("测试类结束之后执行一次")


    baseurl = "https://test-autonomous-saas.deepblueai.com"

    def test_login(self,connect_database):
        url = urljoin(self.baseurl, "/api/athena-auth/oauth/token")
        data = {
            "username":"liudp",
            "password":"e10adc3949ba59abbe56e057f20f883e",
            "grant_type":"password"
        }

        # YamlUtil().write_extract_yaml({'athena_token':Authorization.json()})

        headers = {
            "Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
        }
        response = requests.post(url, headers=headers, data=data)
        # response = requests.post(url, data=data)
        response_dict = response.json()
        # pattern = re.compile(r'"pets":s*[s*([sS]*?)s*]')
        # access_token = re.findall("access_token", response)
        response_data = response_dict.get("data")
        # rep = response_data.get("access_token")
        assert response_data is not None
        # print(response_data)
        YamlUtil().write_extract_yaml({'access_token':response_data['access_token']})
        assert 'access_token' in response_data
        access_token = YamlUtil().read_extract_yaml('access_token')# 别少了函数后面的括号，否则就不是个对象了
        print("access_token is ", access_token)
        assert response_data['user_name'] == 'liudp'
        # print(rep)
        # time.sleep(3)
        print("测试流程完毕")

    def test_rerun(self):
        assert 1 == 1

        # print(response.json())

if __name__ == '__main__':
    pytest.main(['-sv', './scripts', '-n=2', 'reruns=2'])
#
#     # './scripts/test_login.py::TestLogin::test_login', './scripts/test_login.py::test_outclass',