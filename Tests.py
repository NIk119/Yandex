
import allure
from Dat import YandexSeacrhData as dat


# @allure.feature('Open pages')
# @allure.story('Открывает станицу')
# @allure.severity('blocker')
class TestYand:
    @allure.feature('Random Yandex')
    @allure.story('Получаем страницу почты')
    @allure.severity('blocker')
    def test_yandex_search(self,app):
        #запускаем сайт
        app.go_to_site()

    @allure.story('Заходим')
    @allure.severity('blocker')
    def test_yandex_in(self,app):
        app.Yandex.enter_mail()
        #входим на почту
    @allure.story('Логин')
    @allure.severity('critical')
    def test_yandex_login(self,app):
        app.Yandex.enter_login(dat.LOGIN)
        #вводим логин Входим (кнопку нажимаем)
    @allure.story('Пароль')
    @allure.severity('critical')
    def test_yandex_password(self,app):
        app.Yandex.enter_password(dat.PASSWORD)
        #вводим пароль входим в аккаунт
    @allure.story('пошел по почте')
    @allure.severity('normal')
    def test_yandex_mail(self,app):
        app.Yandex.go_mail()
        # пошли по почте
    @allure.story('отправка почты')
    @allure.severity('critical')
    def test_yandex_output(self,app):
        app.Yandex.mail_post(dat.MAIL,dat.LAST_NAME)
        # отправили почту

    



