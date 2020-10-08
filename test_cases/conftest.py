import pytest
from pages.login_and_logout import _login
@pytest.fixture(scope="session")
def login(driver,host):
    _login(driver,host)