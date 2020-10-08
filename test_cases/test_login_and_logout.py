import pytest
from pages.login_and_logout import _login,_logout
class TestLoginAndLogout:

    @pytest.fixture
    def open_page(self,driver,host,request):
        driver.get(host)
        driver.maximize_window()
        def fn():
            driver.delete_all_cookies()
            driver.refresh()
        request.addfinalizer(fn)
        return driver

    @pytest.mark.usefixtures("open_page")
    def test_login_success(self,driver):
        _login(driver)


    def test_login_fail(self,driver):
        _login(driver,"1826878746","Qaz123456!")

    @pytest.mark.usefixtures("login")
    def test_logout_success(self,driver):
        _logout(driver)

if __name__ == "__main__":
    pytest.main(["-s","test_login_and_logout.py"])
