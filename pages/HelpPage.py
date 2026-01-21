from selenium.webdriver import ActionChains
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//div[text()="Сегодня актуально"]')
    REGISTRATION = (By.XPATH, '//div[text()="Регистрация"]')
    MY_PROFILE = (By.XPATH, '//div[text()="Мой профиль"]')
    COMMUNICATION = (By.XPATH, '//div[text()="Общение"]')
    PROFILE_ACCESS = (By.XPATH, '//div[text()="Доступ к профилю"]')
    SECURITY = (By.XPATH, '//div[text()="Безопасность"]')
    GROUPS = (By.XPATH, '//div[text()="Группы"]')
    PAYED_FUNCTIONS = (By.XPATH, '//div[text()="Платные функции"]')
    SPAM = (By.XPATH, '//div[text()="Нарушения и спам"]')
    GAMES_AND_APPS = (By.XPATH, '//div[text()="Игры и приложения"]')
    OTHER_SERVICES = (By.XPATH, '//div[text()="Другие сервисы"]')
    IMPORTANT_INFORMATION = (By.XPATH, '//div[text()="Полезная информация"]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//div[text()="Рекламный кабинет"]')

class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screen_shot()
            self.find_element(HelpPageLocators.SEARCH_FIELD)
            self.find_element(HelpPageLocators.ACTUAL_TODAY)
            self.find_element(HelpPageLocators.REGISTRATION)
            self.find_element(HelpPageLocators.MY_PROFILE)
            self.find_element(HelpPageLocators.COMMUNICATION)
            self.find_element(HelpPageLocators.PROFILE_ACCESS)
            self.find_element(HelpPageLocators.SECURITY)
            self.find_element(HelpPageLocators.GROUPS)
            self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
            self.find_element(HelpPageLocators.SPAM)
            self.find_element(HelpPageLocators.GAMES_AND_APPS)
            self.find_element(HelpPageLocators.OTHER_SERVICES)
            self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
            self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

    def scrollToItem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()

