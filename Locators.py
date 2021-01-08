from selenium.webdriver.common.by import By

class YandexSeacrhLocators():

    LOCATOR_LOGIN_IN_TO_MAIL = (By.XPATH, "//a[contains(@class,'home-link_bold_yes')]")
    LOGIN_MAIL = (By.XPATH, "//input[@id='passp-field-login']")
    click_login = (By.XPATH, "//button[@type='submit']")
    password_mail = (By.XPATH, "//input[@id='passp-field-passwd']")
    click_password = (By.XPATH, "//button[@type='submit']")
    post_mail=(By.XPATH, "//span[@class='mail-ComposeButton-Text']")
    post_login1 = (By.XPATH, "//div[@class='ComposeRecipients-TopRow']//div[@class='composeYabbles']")
    TextField= (By.XPATH, "//div[@class='ComposeSubject']//input[starts-with(@class,'composeTextField ComposeSubject-TextField')]")
    cke_wysiwyg_div= (By.XPATH, "//div[@class='composeReact-MBodyPanels']//div[starts-with(@class,'cke_wysiwyg_div ')]")
    ComposeSendButton_desktop = (By.XPATH, "//div[contains(@class,'ComposeSendButton_desktop')]")

