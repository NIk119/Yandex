
import allure

from allure_commons.types import AttachmentType

# @allure.feature('Open pages')
# @allure.story('Открывает станицу')
# @allure.severity('blocker')
@allure.feature('Random Yandex')
@allure.story('Получаем страницу почты')
@allure.severity('blocker')
def test_yandex_search(app):
    #запускаем сайт
    app.go_to_site()

@allure.story('Заходим')
@allure.severity('blocker')
def test_yandex_in(app):
    app.Yandex.enter_mail()
    #входим на почту
@allure.story('Логин')
@allure.severity('critical')
def test_yandex_login(app):
    app.Yandex.enter_login('cnbrfn')
    #вводим логин Входим (кнопку нажимаем)
@allure.story('Пароль')
@allure.severity('critical')
def test_yandex_password(app):
    app.Yandex.enter_password('adkjgsuiafsiauoyrn1q')
    #вводим пароль входим в аккаунт
@allure.story('пошел по почте')
@allure.severity('normal')
def test_yandex_mail(app):
    app.Yandex.go_mail()
    # пошли по почте
@allure.story('отправка почты')
@allure.severity('critical')
def test_yandex_output(app):
    app.Yandex.mail_post('maketalents@simbirsoft.com','Зотов')
    # отправили почту
    
    



