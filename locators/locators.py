from selenium.webdriver.common.by import By


class IndexPageLocator:
    MAIN_PAGE_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"
    INGREDIENT_MODAL_XPATH = "//section[contains(@class, 'Modal_modal_opened_')]"
    TEMPORARY_ORDER_MODAL_HEADER = (By.XPATH, "//h2[text()='9999']")
    ORDER_ID_XPATH = "//h2[contains(@class, 'Modal_modal__title')]"
    ORDER_LINE = By.XPATH, "//p[text() = 'Лента Заказов']"
    FIRST_ORDER = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]'
    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")
    LOGO = By.XPATH, '//*[@id="root"]/div/header/nav/div/a'
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PRIVATE_AREA = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    CLOSE_MODAL = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    INGREDIENT = By.CSS_SELECTOR, 'a[href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    CLOSE_CONFIRMATION = By.CLASS_NAME, "Modal_modal__P3_V5"
    loc_1 = By.CSS_SELECTOR, '[alt="Флюоресцентная булка R2-D3"]'
    loc_2 = By.CSS_SELECTOR, '[alt="Перетяните булочку сюда (верх)"]'
    RECOVERY_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'
    INGREDIENT_MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    FIRST_INGREDIENT_COUNTER_XPATH = "//p[contains(@class, 'counter_counter')][1]"


class ProfilePageLocators:
    BUTTON_EXIT_ACCOUNT = By.XPATH, "//button[text()='Выход']"
    ORDERS_HISTORY_AREA = By.XPATH, "//a[text()='История заказов']"
    PROFILE_AREA = By.XPATH, "//a[text()='Профиль']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"


class OrderLinePageLocators:
    ORDER_LINE_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                                "'text_type_digits')]")
    ORDER_DETAILS_MODAL = ".//div[contains(@class, 'Modal_orderBox')]"
    ORDER_DETAILS_MODAL_ORDER_ID_XPATH = ".//div[contains(@class, 'Modal_orderBox')]/p"
    TOTAL_COUNT_XPATH = "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_COUNT_XPATH = "//p[text()='Выполнено за сегодня:']/following-sibling::p"


class Input:
    INPUT_EMAIL = By.XPATH, "//input[@name='name']"
    EMAIL_INPUT_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::*"
    INPUT_PASSWORD = By.XPATH, "//input[@name='Пароль']"
    STATIC_PASSWORD = By.XPATH, "//input[@type='password']"


class TextValidation:
    CODE_RECOVERY_TEXT = By.XPATH, "//label[text()='Введите код из письма']"
    HEADERS_H2 = By.XPATH, "//*[@id='root']/div/main/div/h2"
    INDEX_TEXT_H1 = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_TEXT_H1 = (By.XPATH, "//h1[text()='Лента заказов']")
    INGREDIENT_TEXT_H2 = (By.XPATH, "//h2[text()='Детали ингредиента']")
    NUMBER_COUNT = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/div/p'
    ACTUAL_TEXT = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/h2'
    EXPECTED_TEXT = By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div/h2'


class ResetPasswordPageLocators:
    HEADER_RESTORE_PASSWORD = By.XPATH, ".//h2[text()='Восстановление пароля']"
    SHOW_PASSWORD_BUTTON = By.XPATH, ".//div[contains(@class, 'input__icon')]"
    ACTIVE_PASSWORD_INPUT_FIELD = By.XPATH, ".//div[contains(@class, 'input_status_active')]"


class PasswordRecoveryPageLocators:
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM = (By.XPATH, "//a[text()='Войти']")
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//button[text()='Восстановить']")
