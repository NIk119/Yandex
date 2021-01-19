
import allure
from Dat import YandexSeacrhData as dat
from BaseApp import BasePage

# @allure.feature('Open pages')
# @allure.story('Открывает станицу')
# @allure.severity('blocker')
class TestYand:
    @allure.feature('Random Yandex')
    @allure.story('Получаем страницу почты')
    @allure.severity('blocker')
    def test_yandex_search(self,app):
        #аннотацию fixture не принимает (или class)
        #запускаем сайт
        BasePage(app).go_to_site()

    @allure.story('Заходим')
    @allure.severity('blocker')
    def test_yandex_in(self,app):
        BasePage(app).enter_mail()
        #входим на почту
    @allure.story('Логин')
    @allure.severity('critical')
    def test_yandex_login(self,app):
        BasePage(app).enter_login(dat.LOGIN)
        #вводим логин Входим (кнопку нажимаем)
    @allure.story('Пароль')
    @allure.severity('critical')
    def test_yandex_password(self,app):
        BasePage(app).enter_password(dat.PASSWORD)
        #вводим пароль входим в аккаунт
    @allure.story('пошел по почте')
    @allure.severity('normal')
    def test_yandex_mail(self,app):
        BasePage(app).go_mail()
        # пошли по почте
    @allure.story('отправка почты')
    @allure.severity('critical')
    def test_yandex_output(self,app):
        BasePage(app).mail_post(dat.MAIL,dat.LAST_NAME)
        # отправили почту

    



