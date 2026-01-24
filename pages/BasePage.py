from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By



class BasePageLocators:
    LOGO_BUTTON = (By.XPATH, '//*[@class="toolbar_logo_img"]')
    VK_ECO_SYSTEM_BUTTON = (By.XPATH, '//*[@class="toolbar_nav_i_ic"]')
    MORE_BUTTON = (By.XPATH, '//a[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self,driver):
        self.driver = driver


    @allure.step('проверяем корректность загрузки страницы')
    def check_page(self):
        self.attach_screen_shot()
        self.find_element(BasePageLocators.LOGO_BUTTON).click()
        self.find_element(BasePageLocators.VK_ECO_SYSTEM_BUTTON).click()


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

    @allure.step('Нажимаем кнопку эко системы')
    def click_vk_system_button(self):
        self.find_element(BasePageLocators.VK_ECO_SYSTEM_BUTTON).click()

    @allure.step('Нажимаем кнопку "еще"')
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()


    def get_windows_id(self,index):
        return self.driver.window_handles[index]


    def switch_window(self,window_id):
        self.driver.switch_to.window(window_id)