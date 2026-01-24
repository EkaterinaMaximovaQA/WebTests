import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class EcoSystemLocators:
    TITLE_LABEL = (By.XPATH, '//*[@class="title-h2"]')

class EcoSystemPageHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Проверка загрузки страницы')
    def check_page(self):
        self.attach_screen_shot()
        self.driver.find_element(EcoSystemLocators.TITLE_LABEL)





