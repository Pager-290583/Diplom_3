import allure
from pages.base_page import BasePage
from locators.locators import Input, ResetPasswordPageLocators, PasswordRecoveryPageLocators, IndexPageLocator


class RecoveryMetod(BasePage):
    @allure.step('Переход на страницу Восстановление пароля')
    def goto_recovery_password_page(self):
        self.click(IndexPageLocator.RECOVERY_BUTTON)

    @allure.step('Ввод почты')
    def enter_email(self, email):
        self.enter_text(email, Input.EMAIL_INPUT_FIELD)
        self.click(PasswordRecoveryPageLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        self.enter_text(password, Input.STATIC_PASSWORD)

    @allure.step('Нажимаем на кнопку Показать пароль')
    def show_password_click(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Ждем загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_header_loaded(self):
        self.wait_for_element_loaded(PasswordRecoveryPageLocators.HEADER_RESTORE_PASSWORD)
