import pytest
from common.yaml_util import YamlUtil
@pytest.fixture(scope="function")
def connect_database():
    print("连接数据库")
    yield
    print("关闭数据库")# yield，在引用该修饰器函数执行完毕之后，执行yield后面的内容
    #yield作为一个生成器，相当于返回一个对象

@pytest.fixture(scope="session", autouse = True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()