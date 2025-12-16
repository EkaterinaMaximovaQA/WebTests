from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @placeholder="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and contains(@class, "vkuiButton__modePrimary")]')
    QR_CODE_BUTTON = (By.XPATH,'//button[@label="Войти по QR-коду"]')
    LOGIN_PROBLEM_LINK = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER_LINK = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    LOGIN_VK_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_MAIL_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_YANDEX_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//span[contains(@class, "LoginForm-module__error")]')

class LoginPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_PROBLEM_LINK)
        self.find_element(LoginPageLocators.REGISTER_LINK)
        self.find_element(LoginPageLocators.LOGIN_VK_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_MAIL_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_YANDEX_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def enter_login(self,login_text):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login_text) #(send_keys)метод Selenium, который:Имитирует фокус на элементе (как если бы мы кликнули в поле),Имитирует нажатие клавиш на клавиатуре для каждого символа,Последовательно "печатает" переданный текст







