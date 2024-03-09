# import allure
#
# from pages.base_page import BasePage
# from locators.locators import Button, Input, ProfilePageLocators, OrderLinePageLocators
#
#
# class FeedOrderPage(BasePage):
#     @allure.step('если кликнуть на заказ, откроется всплывающее окно с деталями')
#     def goto_history_order(self, name, password):
#         self.enter_text(name, Input.INPUT_EMAIL)
#         self.enter_text(password, Input.INPUT_PASSWORD)
#         self.click(ProfilePageLocators.LOGIN_BUTTON)
#         self.click(Button.AUTH_BUTTON)
#         self.click(ProfilePageLocators.ORDERS_HISTORY_AREA)
#         self.click(OrderLinePageLocators.FIRST_ORDER)
#
#     # @allure.step('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
#     # def order_user_in_history_list(self, name, password):
#     #     self.enter_text(name, Input.INPUT_EMAIL)
#     #     self.enter_text(password, Input.INPUT_PASSWORD)
#     #     self.click(Button.LOGIN_BUTTON)
#     #     self.move(Button.loc_1, Button.loc_2)
#     #     self.click(Button.BUTTON_ADD_ORDER)
#
