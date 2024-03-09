import pytest
import allure


from application import Application
from test_date.constants import Constants
from test_date.user_data import UserData


@allure.title('Браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def app(request):
    with allure.step('Запуск браузера'):
        if request.param == 'chrome':
            app = Application(browser='chrome', base_url=Constants.URL)
        if request.param == 'firefox':
            app = Application(browser='firefox', base_url=Constants.URL)
    yield app
    with allure.step('Закрытие браузера'):
        app.destroy()


@pytest.fixture()
def user_data():
    user_data = UserData()
    return user_data

