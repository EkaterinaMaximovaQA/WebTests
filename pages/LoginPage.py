from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @placeholder="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_CODE_BUTTON = (By.XPATH,'//*[@data-l="t,get_qr"]')
    LOGIN_PROBLEM_LINK = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER_LINK = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide" and @data-l="t,register"]')
    LOGIN_VK_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_MAIL_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_YANDEX_BUTTON = (By.XPATH,'//*[@class="i ic social-icon __s __yandex"]')

class LoginPageHelper(BasePage):
    pass

