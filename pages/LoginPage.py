import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

#Локаторы = Адреса домов

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@id="field_email" and @name="st.email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @placeholder="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and contains(@class, "vkuiButton__modePrimary")]')
    QR_CODE_BUTTON = (By.XPATH,'//button[@label="Войти по QR-коду"]')
    LOGIN_PROBLEM_LINK = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER_LINK = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    LOGIN_VK_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_MAIL_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_YANDEX_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//span[contains(@class, "LoginForm-module__error")]')
    RECOVER_BUTTON = (By.XPATH, '//a[.//span[text()="Восстановить"]]')
    CANCELLATION_BUTTON = (By.XPATH, '//span[@class="vkuButton__content" and text()="Отмена"]')




#Хелперы = Почтальон, который ходит по этим адресам

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




    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screen_shot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON, clickable=True).click()


    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screen_shot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text


    @allure.step('Заполняем поле логин')
    def type_login(self,login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screen_shot()

    @allure.step('Заполняем поле пароля')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screen_shot()

    @allure.step('Переходим к восстановлению')
    def click_recovery (self):
        self.attach_screen_shot()
        time.sleep(10)
        self.find_element(LoginPageLocators.RECOVER_BUTTON).click()

    @allure.step('Переход к регистрации')
    def click_registration(self):
        self.attach_screen_shot()
        self.find_element(LoginPageLocators.REGISTER_LINK).click()










