from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from Locators import YandexSeacrhLocators as YSL
import allure
from allure_commons.types import AttachmentType




class SearchHelper():
    def __init__(self,app):
        self.app=app
        #self.app.browser.implicitly_wait(10)


    def enter_mail(self):
        # заходим на почту
        with allure.step("WebDriverWait явное ожидание"):
            search_field = WebDriverWait(self.app.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'home-link_bold_yes')]")))
        # явное ожидание ,локатор кидаем в него из другого файла
        with allure.step("клик"):
            search_field.click()
        with allure.step("создали переменную окно 0"):
            new_window = self.app.browser.window_handles[0]
        # создали переменную для действия на  вкладках
        with allure.step("создали переменную окно 1"):
            new_window1 = self.app.browser.window_handles[1]
        with allure.step("переключили на окно 0"):
            self.app.browser.switch_to.window(new_window)
        # переключили действия на первую вкладку
        with allure.step("переключили на окно 1"):
            self.app.browser.switch_to.window(new_window1)

    def enter_login(self,login):
        #логин вводим
        time.sleep(5)
        with allure.step("WebDriverWait явное ожидание"):
            search_field = self.app.find_element(YSL.LOGIN_MAIL)
        #запуск явного ожидания через BaseApp
        with allure.step("очистили окно ввода логина"):
            search_field.clear()
        with allure.step("ввели  логин"):
            search_field.send_keys(login)
        self.click_login()


    def click_login(self):
        #кликнули на кнопку
        search_field=self.app.find_element(YSL.click_login)
        with allure.step("Click"):
            search_field.click()

    def enter_password(self,password):
        #пароль вводим
        with allure.step("WebDriverWait явное ожидание"):
            search_field = self.app.find_element(YSL.password_mail)
        with allure.step("очистили окно ввода пароля"):
            search_field.clear()
        with allure.step("ввели  пароль"):
            search_field.send_keys(password)
        self.click_password()

    def click_password(self):
        # кликнули на кнопку
        search_field=self.app.find_element(YSL.click_password)
        with allure.step("Click"):
            search_field.click()

    def count_mail(self):
        #считает письма на конкретной странице
        search_field = self.app.browser.find_elements_by_xpath("//div[starts-with(@class,'ns-view-messages-item-wrap ns-view-id-')]")
        with allure.step("считаем количество писем на странце"):
            return len(search_field)

    def go_mail(self):
        #пошли по почте
        a=len(self.app.browser.find_elements_by_xpath("//div[@data-key='box=messages-pager-date-box']//div[contains(@class,'b-mail-paginator__group js-year')]"))
        #переменная нужна для верхней границы почты (год)
        n=a
        #для указание на год
        aa=0
        #для подсчета почты
        for i in range(a,11,-1):
            #пробегаем по годам
            with allure.step(f"Год {2022-n-1+i}"):
                c=len(self.app.browser.find_elements_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//div[contains(@class,'b-mail-paginator__group js-year')][{i}]/div[contains(@class,'b-mail-paginator__item')]"))
                #количество месяцев
                k=0
                #переменная для нижней границы месяцев
                if i==1:
                    #если год последний (конечный) на почте , то проверь сколько месяцев там есть и поставь эту границу
                    k=12-c+1
                    c=13
                for u in range(c-1,k,-1):
                    #пошли по месяцам
                    with allure.step(f"месяц {u}"):
                        try:
                            #Тут уже идет пробежка по почте и фиксация количества писем, если все же выскакивает ошибка (ElementClickInterceptedException),а она выскакиват
                            if u<10:
                                u=f'0{u}'
                            #search_field=self.app.browser.find_element_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")
                            with allure.step("WebDriverWait явное ожидание"):
                                search_field=WebDriverWait(self.app.browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")))
                            with allure.step("переместились к элементу почта , с помощью java_script"):
                                self.app.browser.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", search_field)
                            with allure.step("Click"):
                                search_field.click()
                            time.sleep(2)
                            with allure.step("Берем из ссылки на сайте наше местоположение по тесту"):
                                v=self.app.browser.current_url
                            #берем из ссылки на сайте наше местоположение по тесту ,для вывода в консоли
                            with allure.step("прибавили к переменной класса , количество писем"):
                                aa+=self.count_mail()
                            print(f'{v[-8:-1]} писем {aa}  по году{i} по месяцу{u}')


                        except ElementClickInterceptedException:
                            with allure.step(f"ElementClickInterceptedException ,отправляем снова запрос"):
                                #Мы ее ловим здесь и снова отправляем запрос
                                #search_field=self.app.browser.find_element_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")
                                with allure.step("WebDriverWait явное ожидание"):
                                    search_field=WebDriverWait(self.app.browser, 120).until(EC.presence_of_element_located((By.XPATH, f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")))
                                with allure.step("переместились к элементу почта , с помощью java_script"):
                                    self.app.browser.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", search_field)
                                with allure.step("Click"):
                                    search_field.click()
                                time.sleep(2)
                                with allure.step("Берем из ссылки на сайте наше местоположение по тесту"):
                                    v=self.app.browser.current_url
                                with allure.step("прибавили к переменной класса , количество писем"):
                                    aa+=self.count_mail()
                                print(f'ошибка:ElementClickInterceptedException {v[-8:-1]} писем {aa}  по году{i} по месяцу{u}')
                        with allure.step("Делаем скриншот"):
                            allure.attach(self.app.browser.get_screenshot_as_png(), name=f"Год {2022-n-1+i},месяц {u}",attachment_type=AttachmentType.PNG)
                                #Фиксируем результаты в allure

        self.countmails=aa
        #записали весь результат в переменную(класса)

    def mail_post(self,post_login,fam):
        #Отправляем почту ,в нее подаем 2 аргумена(почту и фамилию)
        #self.app.browser.implicitly_wait(10)
        time.sleep(3)
        with allure.step("Click"):
            self.app.find_element(YSL.post_mail).click()
        with allure.step("Отправляем mail получателя"):
            self.app.find_element(YSL.post_login1).send_keys(post_login)
        #здесь нужно отметьтить то ,что если сделать здесь задержку в отправке письма, то высветится окошко выбора mail, а оно перекрывает остальные окна
        #значит нужно реализовать код иначе, но так как это было замечено случайно , то лучше реализовать это потом

        search_field=self.app.find_element(YSL.cke_wysiwyg_div)
        with allure.step("Click"):
            search_field.click()
        with allure.step("В теле письма пишем"):
            search_field.send_keys(f"Количество писем: {self.countmails}")
        with allure.step("Заголовок пишем"):
            self.app.find_element(YSL.TextField).send_keys(f"Тестовое  задание.  {fam}")
        with allure.step("Click"):
            self.app.find_element(YSL.ComposeSendButton_desktop).click()
        time.sleep(5)
