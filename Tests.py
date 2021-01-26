
import allure
from Dat import YandexSeacrhData as dat
from BaseApp import BaseApp
from selenium.webdriver.common.by import By
# @allure.feature('Open pages')
# @allure.story('Открывает станицу')
# @allure.severity('blocker')
# def step_back(fn):
#     def wrapper(self,app):
#         if BasePage(app).browser.current_url == "https://mail.yandex.ru/?uid=104630247#inbox":
#             fn(self)
#
#             BasePage(app).enter_password(dat.PASSWORD)
#             fn(self)
#
#             BasePage(app).enter_mail()
#             BasePage(app).enter_login(dat.LOGIN)
#             BasePage(app).enter_password(dat.PASSWORD)
#             fn(self)
#     return  wrapper()
class TestYand:
    @allure.feature('Random Yandex')
    @allure.story('Получаем страницу почты')
    @allure.severity('blocker')
    def test_yandex_search(self,app):
        #аннотацию fixture не принимает (или class)
        #запускаем сайт
        BaseApp(app).go_to_site()
        #a=BasePage(app).proverka_url("https://yandex.ru/")
        #print(a)
    @allure.story('Заходим')
    @allure.severity('blocker')
    def test_yandex_in(self,app):
        #print(BasePage(app).proverka_url("https://yandex.ru/"))
        if BaseApp(app).proverka_url("https://yandex.ru/"):
            BaseApp(app).enter_mail()

        else:
            BaseApp(app).go_to_site()
            BaseApp(app).enter_mail()
            #входим на почту
    @allure.story('Логин')
    @allure.severity('critical')
    def test_yandex_login(self,app):
        #print(BasePage(app).proverka_url_changes('https://passport.yandex.ru/auth/welcome?'))

        if BaseApp(app).proverka_url_changes('https://passport.yandex.ru/auth/welcome?') :
            #print(BasePage(app).proverka_url('https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru'))
            #print(BasePage(app).browser.current_url == "https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru")
            print('1')
            BaseApp(app).enter_login(dat.LOGIN)
        elif BaseApp(app).proverka_url("https://yandex.ru/"):
            #print(BasePage(app).browser.current_url == "https://yandex.ru/")
            print('2')
            if BaseApp(app).proverka_avtorizacii() :
                print('4')
                #print(BasePage(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)

        else:
            BaseApp(app).go_to_site()
            print('22')
            if BaseApp(app).proverka_avtorizacii() :
                print('4')
                print(BaseApp(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                # else:
                #     print(BasePage(app).browser.current_url != "https://yandex.ru/")
                #     print('3')
                #     BasePage(app).go_to_site()
                #     BasePage(app).enter_mail()
                #     BasePage(app).enter_login(dat.LOGIN)


            # else:

        # BasePage(app).enter_login(dat.LOGIN)
        #вводим логин Входим (кнопку нажимаем)
    @allure.story('Пароль')
    @allure.severity('critical')
    def test_yandex_password(self,app):
        if BaseApp(app).proverka_url('https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru'):


            print(BaseApp(app).browser.current_url == "https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru")
            print('1')
            #BasePage(app).enter_login(dat.LOGIN)
            BaseApp(app).enter_password(dat.PASSWORD)
        elif BaseApp(app).proverka_url("https://yandex.ru/"):
            # print(BasePage(app).browser.current_url == "https://yandex.ru/")
            print('2')
            if BaseApp(app).proverka_avtorizacii():
                print('4')
                # print(BasePage(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                BaseApp(app).enter_password(dat.PASSWORD)
            else:
                BaseApp(app).go_to_site()
                print('22')
                if BaseApp(app).proverka_avtorizacii():
                    print('4')
                    print(BaseApp(app).proverka_avtorizacii())
                    BaseApp(app).enter_mail()
                    BaseApp(app).enter_login(dat.LOGIN)
                    BaseApp(app).enter_password(dat.PASSWORD)
        #вводим пароль входим в аккаунт
    @allure.story('пошел по почте')
    @allure.severity('normal')
    def test_yandex_mail(self,app):
        if BaseApp(app).proverka_url("https://mail.yandex.ru/?uid=104630247#inbox"):
            print(BaseApp(app).browser.current_url == "https://mail.yandex.ru/?uid=104630247#inbox")
            print('1')
            #BasePage(app).enter_login(dat.LOGIN)
            BaseApp(app).go_mail()
        elif BaseApp(app).proverka_url("https://yandex.ru/"):
            # print(BasePage(app).browser.current_url == "https://yandex.ru/")
            print('2')
            if BaseApp(app).proverka_avtorizacii():
                print('4')
                # print(BasePage(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                BaseApp(app).enter_password(dat.PASSWORD)
                BaseApp(app).go_mail()
        else:
            BaseApp(app).go_to_site()
            print('22')
            if BaseApp(app).proverka_avtorizacii():
                print('4')
                print(BaseApp(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                BaseApp(app).enter_password(dat.PASSWORD)
                BaseApp(app).go_mail()
        # пошли по почте
    @allure.story('отправка почты')
    @allure.severity('critical')
    def test_yandex_output(self,app):
        if BaseApp(app).proverka_url_changes("https://mail.yandex.ru/?uid="):
            #print(BasePage(app).browser.current_url == "https://mail.yandex.ru/?uid=")
            print('1')
            if BaseApp(app).proverka_count_mail():
                BaseApp(app).mail_post(dat.MAIL, dat.LAST_NAME)
            else:
                BaseApp(app).go_mail()
                BaseApp(app).mail_post(dat.MAIL, dat.LAST_NAME)
            #BasePage(app).enter_login(dat.LOGIN)
            # BaseApp(app).mail_post(dat.MAIL, dat.LAST_NAME)
        elif BaseApp(app).proverka_url("https://yandex.ru/"):
            # print(BasePage(app).browser.current_url == "https://yandex.ru/")
            print('2')
            if BaseApp(app).proverka_avtorizacii():
                print('4')
                # print(BasePage(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                BaseApp(app).enter_password(dat.PASSWORD)
                BaseApp(app).go_mail()
            BaseApp(app).mail_post(dat.MAIL, dat.LAST_NAME)
        else:
            BaseApp(app).go_to_site()
            print('22')
            if BaseApp(app).proverka_avtorizacii():
                print('4')
                print(BaseApp(app).proverka_avtorizacii())
                BaseApp(app).enter_mail()
                BaseApp(app).enter_login(dat.LOGIN)
                BaseApp(app).enter_password(dat.PASSWORD)
                BaseApp(app).go_mail()
                BaseApp(app).mail_post(dat.MAIL, dat.LAST_NAME)
        # отправили почту

    



