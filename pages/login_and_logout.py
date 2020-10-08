"""
@author = Catcus Hu
@store = "用户登录退出业务"
@date = 2020-10-08
"""

from lib.base import Base


"""元素定位"""
loc_userName = ("css selector",".pass-text-input-userName")
loc_psw = ("css selector",".pass-text-input-password")
loc_submit_btn = ("css selector",".pass-button-submit")

loc_login_success = ("css selector",".KQcHyA")

loc_logout = ("xpath","//a[@node-type ='login-out']")


def _login(driver,username="18268878747",psw="Qaz123456!"):
    base = Base(driver)
    # driver.get(host)  ## 在这边在写一次打开网址，会导致运行脚本时多次打开空白网页
    base.send_words(loc_userName,username)
    base.send_words(loc_psw,psw)
    base.click(loc_submit_btn)

def _login_result(driver):
    base = Base(driver)
    base.assert_element_is_display(loc_login_success)

def _logout(driver):
    base = Base(driver)
    # driver.get(host+"/disk/home?")
    base.click(loc_logout)

def _logout_result(driver):
    base = Base(driver)
    base.assert_is_title("百度网盘")

