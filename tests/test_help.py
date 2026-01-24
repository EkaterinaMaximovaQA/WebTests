import allure

from core.BaseTests import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper


BASE_URL = 'https://ok.ru/help'

def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)