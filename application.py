import allure
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.recovery_metod import RecoveryMetod
from pages.designer_page import DesignerPage
from asserts.base_assert import BaseAsserts
from pages.profile_page import ProfilePage
from pages.oreder_history_page import OrdersHistoryPage
from pages.order_line_page import OrderLinePage


class Application:

    def __init__(self, browser, base_url):
        self.base_url = base_url
        self.base = BasePage(self)
        self.login_page = LoginPage(self)
        self.recovery_metod = RecoveryMetod(self)
        self.designer_page = DesignerPage(self)
        self.profile_page = ProfilePage(self)
        self.order_history_page = OrdersHistoryPage(self)
        self.order_line_page = OrderLinePage(self)
        self.base_asserts = BaseAsserts(self)
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)

    @allure.step('Завершение сессии')
    def destroy(self):
        self.wd.quit()

