import allure

from pages.base_page import BasePage
from locators.locators import Input, IndexPageLocator, ProfilePageLocators


class LoginPage(BasePage):
    @allure.step('переход по клику на «Личный кабинет»')
    def login(self, name, password):
        self.enter_text(name, Input.INPUT_EMAIL)
        self.enter_text(password, Input.INPUT_PASSWORD)
        self.click(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('переход в раздел «История заказов»')
    def goto_history(self):
        self.click(IndexPageLocator.PRIVATE_AREA)
        self.click(ProfilePageLocators.ORDERS_HISTORY_AREA)

    @allure.step('выход из аккаунта.')
    def logout_profile(self):
        self.click(IndexPageLocator.PRIVATE_AREA)
        self.click(ProfilePageLocators.BUTTON_EXIT_ACCOUNT)
