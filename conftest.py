import pytest
from BaseApp import BasePage

@pytest.fixture(scope="session")
def app(request):
    fix = BasePage()
    def close_driver():
        fix.browser.quit()
    request.addfinalizer(close_driver)
    return fix

