import allure

from pages.base_page import BasePage
from locators.locators import IndexPageLocator


class DesignerPage(BasePage):
    @allure.step('переход по клику на «Конструктор»')
    def designer_page(self):
        self.click(IndexPageLocator.MENU_CONSTRUCTOR)

    @allure.step('переход по клику на «Лента заказов»')
    def order_page(self):
        self.click(IndexPageLocator.ORDER_LINE)

    @allure.step('всплывающее окно закрывается кликом по крестику')
    def modal_ingredient(self):
        self.click(IndexPageLocator.INGREDIENT)

    @allure.step('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def add_ingredient(self):
        self.click(IndexPageLocator.INGREDIENT)

    @allure.step('всплывающее окно закрывается кликом по крестику')
    def close_ingredient(self):
        self.click(IndexPageLocator.INGREDIENT)

    @allure.step('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def drug_and_drup_ingredient(self):
        self.move(IndexPageLocator.loc_1, IndexPageLocator.loc_2)

