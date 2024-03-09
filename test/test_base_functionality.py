import allure
from locators.locators import TextValidation, IndexPageLocator


@allure.epic('Проверка основного функционала')
class TestBaseFunction:

    @allure.title('переход по клику на «Конструктор»')
    def test_goto_designer_page(self, app):
        app.base.open('/')
        elm = app.wd.find_element(*TextValidation.INDEX_TEXT_H1).text
        assert elm == 'Соберите бургер'

    @allure.title('переход по клику на «Лента заказов»')
    def test_goto_order_pager(self, app, user_data):
        app.base.open('/feed')
        elm = app.wd.find_element(*TextValidation.FEED_TEXT_H1).text
        assert elm == 'Лента заказов'

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_modal_ingredient(self, app):
        app.base.open('/')
        app.base.click(IndexPageLocator.INGREDIENT)
        elm = app.wd.find_element(*TextValidation.INGREDIENT_TEXT_H2).text
        assert elm == 'Детали ингредиента'

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_close_modal_window(self, app):
        app.base.open('/')
        app.base.click(IndexPageLocator.INGREDIENT)
        app.base.click_close_modal()
        assert app.base_asserts.are_exist(IndexPageLocator.CLOSE_CONFIRMATION)

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_drug_and_drop(self, app):
        app.base.open('/')
        app.base.move(IndexPageLocator.loc_1, IndexPageLocator.loc_2)
        count = len(app.wd.find_element(*TextValidation.NUMBER_COUNT).text)
        assert count > 0

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_login_user_make_order(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.base.move(IndexPageLocator.loc_1, IndexPageLocator.loc_2)
        app.base.click(IndexPageLocator.BUTTON_MAKE_ORDER)
        assert app.base_asserts.check_modal_opened()
