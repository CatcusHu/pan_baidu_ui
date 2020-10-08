"""
@author = Catcus Hu
@store = "公共方法封装"
@date = 2020-10-08
"""

import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    MAX_TIME = 10
    def __init__(self,driver,timeout=10,timesleep=0.5):
        self.driver = driver
        self.timeout = timeout
        self.timesleep = timesleep

    # def open_browser(self,current_url):
    #     self.driver.get(current_url)
    #     return self.driver.maximize_window()

    def wait(self,fn):
        """隐式时间等待装饰器"""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > self.MAX_TIME:
                    raise e
                time.sleep(0.5)

    def find_element(self,locator):
        if not isinstance(locator,tuple):
            print("请输入元祖类型数据类型")
        else:
            return WebDriverWait(self.driver,self.timeout,self.timesleep).until((EC.presence_of_element_located(locator)))

    def find_elements(self,locator):
        if not isinstance(locator,tuple):
            print("请输入元祖类型数据类型")
        else:
            try:
                return WebDriverWait(self.driver,self.timeout,self.timesleep).until(EC.presence_of_all_elements_located(locator))
            except:
                return []

    def click(self,locator):
        return self.find_element(locator).click()

    def send_words(self,locator,text):
        return self.find_element(locator).send_keys(text)

    def assert_is_title(self,assert_text):
        assert assert_text in self.driver.title

    def assert_element_is_display(self,locator):
        return self.find_element(locator).is_displayed()

# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     base = Base(driver)
#     base.open_browser("https://www.baidu.com")
#     base.wait(lambda: time.sleep(0.5))
#     base.assert_is_title("百度一下")
#     base.send_words(("id","kw"),"hello")
#     base.click(("id","su"))
#     base.wait(lambda :time.sleep(0.5))
#     base.assert_element_is_display(("css selector",".soutu-btn"))
#     base.quit_browser()

