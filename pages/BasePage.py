from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,locator, time=5, clickable = False):
        if clickable:
            return WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(locator),
                                                         message=f'не удалось найти локатор {locator}')
        else:
            return WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(locator),
                                                         message=f'не удалось найти локатор {locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_all_elements_located(locator),
            message=f"Не удалось найти элементы {locator}"
        )

    @allure.step('Открываем страницу')
    def get_url(self,url):
        return self.driver.get(url)


    def attach_screen_shot(self):
        allure.attach(self.driver.get_screenshot_as_png(),'скриншот',allure.attachment_type.PNG)


