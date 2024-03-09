import allure
from locators.locators import TextValidation, ResetPasswordPageLocators


@allure.epic('Восстановление пароля')
class TestRecoveryPassword:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_goto_recovery_page(self, app, user_data):
        app.base.open('/login')
        app.recovery_metod.goto_recovery_password_page()
        elm = app.wd.find_element(*TextValidation.HEADERS_H2).text
        assert elm == 'Восстановление пароля'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_recovery_password(self, app, user_data):
        app.base.open('/login')
        app.recovery_metod.goto_recovery_password_page()
        app.recovery_metod.enter_email(user_data.EMAIL)
        app.recovery_metod.wait_for_recovery_page_header_loaded()
        elm = app.wd.find_element(*TextValidation.CODE_RECOVERY_TEXT).text
        assert elm == 'Введите код из письма'

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_icon_eyes(self, app, user_data):
        app.base.open('/login')
        app.recovery_metod.goto_recovery_password_page()
        app.recovery_metod.enter_email(user_data.EMAIL)
        app.recovery_metod.wait_for_recovery_page_header_loaded()
        app.recovery_metod.enter_password(user_data.PASSWORD)
        app.recovery_metod.show_password_click()
        assert app.base_asserts.are_exist(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT_FIELD)

