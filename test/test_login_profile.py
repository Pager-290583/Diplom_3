import allure

from locators.locators import IndexPageLocator
from test_date.constants import Constants


@allure.epic('Личный кабинет')
class TestAuthProfileUser:
    @allure.title('переход по клику на «Личный кабинет»')
    def test_auth(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        elm = app.wd.find_element(*IndexPageLocator.BUTTON_MAKE_ORDER).text
        assert elm == 'Оформить заказ'

    @allure.title('переход в раздел «История заказов»')
    def test_goto_history_page(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.login_page.goto_history()
        link = app.wd.current_url
        assert link == Constants.LINK_HISTORY_PASS

    @allure.title('выход из аккаунта')
    def test_logout_profile(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.login_page.logout_profile()
        app.base.click(IndexPageLocator.LOGO)
        text = app.wd.find_element(*IndexPageLocator.MAIN_PAGE_HEADER).text
        assert text == 'Соберите бургер'
