from selenium.webdriver.common.by import By


class OrderPageLocators:
    """
    Форма 'Для кого самокат'
    """
    TEXT_WHO_IS_THE_SCOOTER_FOR = (By.XPATH, ".//div[text()='Для кого самокат']")

    ORDER_FORM_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")

    ORDER_FORM_SECOND_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")

    ORDER_FORM_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")

    ORDER_FORM_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    CHOOSE_METRO_STATION = (By.XPATH, ".//li[@data-value='1']")

    ORDER_FORM_TELEPHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    BUTTON_FURTHER = (By.XPATH, ".//button[text()='Далее']")

    """
    Форма 'Про аренду'
    """
    TEXT_ABOUT_RENT = (By.XPATH, ".//div[text()='Про аренду']")

    ABOUT_RENT_FORM_WHEN_TO_DELIVER_THE_ORDER = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    ABOUT_RENT_FORM_WHEN_TO_DELIVER_THE_ORDER_DATA = (
        By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected') and text()='25']")

    ABOUT_RENT_FORM_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    ABOUT_RENT_FORM_RENTAL_PERIOD_LIST = (By.XPATH, ".//div[text()='сутки']")

    CHECKBOXES_BLACK = (By.XPATH, ".//label[@for='black']")

    ABOUT_RENT_FORM_COMMENT_FOR_THE_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    ABOUT_RENT_FORM_BUTTON_ORDER = (By.XPATH, ".//button[text()='Назад']/following-sibling::button[text()='Заказать']")

    """
    - HEADER
    """
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")
    BUTTON_ORDER = (By.XPATH, "//button[text()='Статус заказа']/preceding-sibling::button[text()='Заказать']")

    """
    Модальное окно хотите оформить заказ?
    """
    BUTTON_YES_WANT_TO_PLACE_AN_ORDER = (By.XPATH, ".//button[text()='Да']")
    BUTTON_NO_WANT_TO_PLACE_AN_ORDER = (By.XPATH, ".//button[text()='Нет']")

    """
    Модальное окно "Заказ оформлен"
    """
    FORM_ORDER_IS_PROCESSED = (By.XPATH, ".//div[text()='Заказ оформлен']")
    BUTTON_VIEW_STATUS = (By.XPATH, ".//button[text()='Посмотреть статус']")

    """
    Локатор для сайта Яндекс Дзен
    """
    YANDEX_DZEN_LOCATOR = (By.XPATH, ".//div[text()='Удобный и быстрый Яндекс Браузер']")

