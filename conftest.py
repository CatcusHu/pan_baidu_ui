"""
@author = Catcus Hu
@store = "全局配置函数
    1.配置浏览器驱动
    2.打开测试站点，并在结束运行测试用例结束后自动关闭
    3.定制测试报告
"
@date = 2020-10-08
"""

import pytest
from selenium import webdriver

_driver = None

def pytest_addoption(parser):
    """全局配置浏览器及默认站点"""
    parser.addoption(
        "--browser",action="store",default="firefox",help="browser option:firefox or chrome"
    )
    parser.addoption(
        "--host",action="store",default="https://pan.baidu.com",help="test-host:https://pan.baidu.com"
    )

@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver"""
    global _driver
    if _driver is None:
        browser_type = request.config.getoption("--browser")
        if browser_type.lower() == "firefox":
            _driver = webdriver.Firefox()
        elif browser_type.lower() == "chrome":
            _driver = webdriver.Chrome()
    def fn():
        _driver.quit()
    request.addfinalizer(fn)
    return _driver

@pytest.fixture(scope="session")
def host(request):
    """定义全局站点地址"""
    return request.config.getoption("--host")