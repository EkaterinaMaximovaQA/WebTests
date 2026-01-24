import allure

from core.BaseTests import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.EcoSystemPage import EcoSystemPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_system_button()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window_id)
    VKEcosystemPage = EcoSystemPageHelper(browser)
    VKEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)
