from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from YandexPages import SearchHelper
class BasePage:

    def __init__(self):
        #self.browser =  webdriver.Firefox()
        self.browser = webdriver.Remote(command_executor="http://192.168.0.101:4444/wd/hub",desired_capabilities={"browserName": "firefox",})
        #в качестве примера испольузется обычный браузер , а ниже сам selenium grid (настроенный)
        self.base_url = "https://yandex.ru/"
        self.countmails=0
        #Переменная для подсчета писем
        self.Yandex=SearchHelper(self)
        self.browser.implicitly_wait(10)
    def find_element(self, locator,time=10):
        return WebDriverWait(self.browser,time).until(EC.visibility_of_element_located(locator),message=f"Can't find element by locator {locator}")
        #чтобы часто не использовать этот метод в YandexPages,я просто буду ссылаться на него

    def go_to_site(self):
        return self.browser.get(self.base_url)


