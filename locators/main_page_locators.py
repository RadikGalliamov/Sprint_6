from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    - HEADER
    """
    BUTTON_ORDER_HEADER = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    """
    - MAIN AREA
    """
    BUTTON_ORDER_MAIN_AREA = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")

    """
    - FOOTER
    """
    COOKIE_BUTTON = (By.XPATH, ".//button[text()='да все привыкли']")

    TEXT_QUESTIONS_ABOUT_IMPORTANT_THINGS = (By.XPATH, ".//div[text()='Вопросы о важном']")
    """
    ACCORDION_BUTTON
    """
    HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY = (By.XPATH, ".//div[@id='accordion__heading-0']")  # добавить описание
    TEXT_HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY = (By.XPATH, ".//div[@id='accordion__panel-0']/p")

    I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE = (By.XPATH, ".//div[@id='accordion__heading-1']/..")
    TEXT_I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE = (By.XPATH, ".//div[@id='accordion__panel-1']/p")

    HOW_IS_RENTAL_TIME_CALCULATED = (By.XPATH, ".//div[@id='accordion__heading-2']")
    TEXT_HOW_IS_RENTAL_TIME_CALCULATED = (By.XPATH, ".//div[@id='accordion__panel-2']/p")

    IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY = (By.XPATH, ".//div[@id='accordion__heading-3']")
    TEXT_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY = \
        (By.XPATH, ".//div[@id='accordion__panel-3']/p")

    IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER = (By.XPATH, ".//div[@id='accordion__heading-4']")
    TEXT_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER = \
        (By.XPATH, ".//div[@id='accordion__panel-4']/p")

    DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER = (By.XPATH, ".//div[@id='accordion__heading-5']")
    TEXT_DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER = (By.XPATH, ".//div[@id='accordion__panel-5']/p")

    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER = (By.XPATH, ".//div[@id='accordion__heading-6']")
    TEXT_IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER = (By.XPATH, ".//div[@id='accordion__panel-6']/p")

    I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT = (By.XPATH, ".//div[@id='accordion__heading-7']")
    TEXT_I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT = (By.XPATH, ".//div[@id='accordion__panel-7']/p")
