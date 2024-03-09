from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import allure
from selenium.common import NoSuchElementException


class BaseAsserts(BasePage):
    def element_text_is_correct(self, text: str, locator: list):
        text_element = self.app.wd.find_element(*locator).text
        assert text_element == text, f"Ожидаемый текст: {text_element}. Фактический текст: {text}"
        return True

    @staticmethod
    def text_is_equal(actual_text: str, expected_text: str):
        assert actual_text == expected_text, f"Фактический текст: {actual_text}, Ожидаемый текст: {expected_text}"
        return True

    @allure.step('Проверка отображения элементов на странице')
    def are_exist(self, locator: list) -> bool:
        assert len(self.app.wd.find_elements(*locator)) > 0, f'Элемент не отображается на странице'
        return True

    @allure.step('Проверяем наличие ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        locator = f"//li[text()='{order_id}']"
        try:
            self.app.wd.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверяем видимость модального окна')
    def check_modal_opened(self):
        try:
            self.app.wd.find_element(By.XPATH, "//section[contains(@class, 'Modal_modal_opened_')]")
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверяем наличие ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_line(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        try:
            self.app.wd.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True
