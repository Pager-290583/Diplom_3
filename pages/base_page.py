import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.locators import IndexPageLocator


class BasePage:

    def __init__(self, app):
        self.app = app

    @allure.step('Открытие страницы')
    def open(self, url: str):
        self.app.wd.get(f"{self.app.base_url}{url}")

    @allure.step('Кликаем по кнопке')
    def click(self, locator):
        self.app.wd.find_element(*locator).click()

    @allure.step('Кликаем по элементу')
    def click_element_located(self, locator, time=10):
        return WebDriverWait(self.app, time).until(ec.presence_of_element_located(locator),
                                                   message=f'Element not found in {locator}').click()

    @allure.step('Ввод текста')
    def enter_text(self, text: str, locator: list):
        self.app.wd.find_element(*locator).send_keys(text)

    @allure.step('Драг-н-дроп элемента на элемент')
    def do_drag_n_drop(self, source, target):
        drag = WebDriverWait(self.app.wd, 20).until(ec.element_to_be_clickable(source))
        drop = WebDriverWait(self.app.wd, 20).until(ec.element_to_be_clickable(target))
        ActionChains(self.app.wd).drag_and_drop(drag, drop).perform()

    @allure.title('Перемещение элемента')
    def move(self, locator_source, locator_target):
        action = ActionChains(self.app.wd)
        source = self.app.wd.find_element(*locator_source)
        target = self.app.wd.find_element(*locator_target)
        action.drag_and_drop(source, target)

    def get_element_text(self, locator):
        elm_text = self.app.wd.find_element(*locator).text
        return elm_text

    @allure.step('Показать /Сткрыть пароль')
    def click_eyes(self, locator):
        self.app.wd.find_element(*locator).click()

    @allure.step('Нажимаем на кнопку Показать пароль')
    def show_password_click(self, locator):
        self.click(*locator)

    @allure.step('Проверяем активность поля ввода пароля')
    def show_password_check(self, locator):
        return self.find_element_located(*locator)

    @allure.step('Ищем элемент по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.app.wd, time).until(ec.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Ждем загрузки заголовка страницы')
    def wait_for_element_loaded(self, locator):
        return WebDriverWait(self.app.wd, 3).until(ec.visibility_of_element_located(locator))

    @allure.step('Ждем загрузки заголовка главной страницы проекта')
    def wait_for_main_page_header_loaded(self):
        self.wait_for_element_loaded(IndexPageLocator.MAIN_PAGE_HEADER)

    @allure.step('Перетаскиваем первый ингредиент в корзину')
    def drag_n_drop_first_ingredient_to_basket(self):
        self.do_drag_n_drop(source=IndexPageLocator.FIRST_INGREDIENT, target=IndexPageLocator.BASKET)

    @allure.step('Кликаем Оформить заказ')
    def click_make_order(self):
        self.click(IndexPageLocator.BUTTON_MAKE_ORDER)

    @allure.step('Создаем заказ')
    def make_order(self):
        self.drag_n_drop_first_ingredient_to_basket()
        self.click_make_order()

    @allure.step('Ждем исчезновения элемента из DOMа')
    def wait_until_element_not_present(self, locator):
        WebDriverWait(self.app.wd, 20).until(ec.invisibility_of_element_located(locator))

    @allure.step('Получаем значение ID заказа при его оформлении')
    def get_order_id_when_created(self):
        self.wait_until_element_not_present(IndexPageLocator.TEMPORARY_ORDER_MODAL_HEADER)
        return self.app.wd.find_element(IndexPageLocator.ORDER_ID_XPATH).text

    @allure.step('Кликаем Лента Заказов')
    def click_orders_line(self):
        self.click(IndexPageLocator.ORDER_LINE)

    @allure.step('Нажимаем на крестик, закрывающий модальное окно')
    def click_close_modal(self):
        self.wait_for_element_loaded(IndexPageLocator.CLOSE_MODAL).click()

    @allure.step('Кликаем по кнопке Личный кабинет')
    def click_private_area_button(self):
        self.click_element_located(IndexPageLocator.PRIVATE_AREA)

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element_located(IndexPageLocator.LOGO)
