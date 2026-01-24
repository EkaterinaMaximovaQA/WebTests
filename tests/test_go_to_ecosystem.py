import allure

from core.BaseTests import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.EcoSystemPage import EcoSystemPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    basePage = BasePageHelper(browser)
    basePage.get_url(BASE_URL)
    basePage.check_page()
    loginPage = LoginPageHelper(browser)
    current_window_id = loginPage.get_windows_id(0)
    loginPage.click_vk_system_button()
    loginPage.click_more_button()
    new_window_id = loginPage.get_windows_id(1)
    loginPage.switch_window(new_window_id)
    vKEcosystemPage = EcoSystemPageHelper(browser)
    vKEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)
