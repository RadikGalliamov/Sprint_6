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

    ABOUT_RENT_FORM_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    ABOUT_RENT_FORM_RENTAL_PERIOD_LIST = (By.XPATH, ".//div[text()='сутки']")

    ABOUT_RENT_FORM_COMMENT_FOR_THE_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    ABOUT_RENT_FORM_BUTTON_ORDER = (By.XPATH, ".//button[text()='Назад']/following-sibling::button[text()='Заказать']")

    """
    - HEADER
    """

    BUTTON_ORDER = (By.XPATH, "//button[text()='Статус заказа']/preceding-sibling::button[text()='Заказать']")