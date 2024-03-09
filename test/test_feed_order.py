import allure
from locators.locators import TextValidation, ProfilePageLocators, IndexPageLocator


@allure.epic('Раздел «Лента заказов»')
class TestFeedOrder:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_last_order(self, app):
        app.base.open('/')
        app.base.click(IndexPageLocator.ORDER_LINE)
        app.base.click(IndexPageLocator.FIRST_ORDER)
        actual_text = app.base.get_element_text(TextValidation.ACTUAL_TEXT)
        expected_text = app.base.get_element_text(TextValidation.EXPECTED_TEXT)
        app.base_asserts.text_is_equal(actual_text, expected_text)

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_new_order_appears_orders_line(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.base.wait_for_main_page_header_loaded()
        app.base.make_order()
        order_id = app.base.get_order_id_when_created()
        app.base.click_close_modal()
        app.base.click(IndexPageLocator.PRIVATE_AREA)
        app.base.wait_for_element_loaded(ProfilePageLocators.PROFILE_AREA)
        app.base.click(ProfilePageLocators.ORDERS_HISTORY_AREA)
        app.order_history_page.click_orders_line()
        app.order_line_page.wait_for_orders_line_header_loaded()
        assert app.base_asserts.check_order_id_in_orders_line(order_id)

    @allure.title('Заказы Выполнено за всё время и Выполнено за сегодня')
    def test_new_order_increases_total_and_today_orders_count(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.base.wait_for_main_page_header_loaded()
        app.base.click_orders_line()
        app.order_line_page.wait_for_orders_line_header_loaded()
        total_count = app.order_line_page.get_total_count()
        today_count = app.order_line_page.get_today_count()
        app.base.click(IndexPageLocator.MENU_CONSTRUCTOR)
        app.base.make_order()
        app.base.click_close_modal()
        app.base.click(IndexPageLocator.ORDER_LINE)
        app.order_line_page.wait_for_orders_line_header_loaded()
        new_total_count = app.order_line_page.get_total_count()
        new_today_count = app.order_line_page.get_today_count()
        assert new_total_count > total_count and new_today_count > today_count

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_processing_orders(self, app, user_data):
        app.base.open('/login')
        app.login_page.login(user_data.EMAIL, user_data.PASSWORD)
        app.base.wait_for_main_page_header_loaded()
        app.base.make_order()
        order_id = app.base.get_order_id_when_created()
        app.base.click_close_modal()
        app.base.click_orders_line()
        assert app.base_asserts.check_order_id_in_processing_orders(order_id)
