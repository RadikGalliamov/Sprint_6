import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPageHelper(BasePage):

    @allure.step("Скроллинг страницы до элемента текст 'Вопросы о важном' на главной странице")
    def scroll_text_questions_about_important_things(self):
        self.scroll_to_element(MainPageLocators.TEXT_QUESTIONS_ABOUT_IMPORTANT_THINGS)

    @allure.step("Элемент 'Сколько это стоит? И как оплатить?'кликабельный")
    def element_clickable(self):
        self.wait_for_clickable(MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY).click()

    @allure.step("Клик по кнопке 'Заказать' в шапке страницы на главной странице")
    def click_order_from_header_main_page(self):
        self.wait_for_clickable(MainPageLocators.BUTTON_ORDER_HEADER).click()


    @allure.step("Клик по кнопке 'Заказать' в основной части странице на главной странице")
    def click_order_from_main_arena_main_page(self):
        self.wait_for_clickable(MainPageLocators.BUTTON_ORDER_MAIN_AREA).click()

    @allure.step("Открыть главную страницу, закрыть куки, кликнуть на кнопку Заказать в шапке сайте")
    def open_page_close_cookie_click_order_from_header_main_page(self):
        self.open()
        self.close_cookie()
        self.click_order_from_header_main_page()

    @allure.step(
        "Открыть главную страницу, закрыть куки, кликнуть на кнопку Заказать в основной части главной страницы")
    def open_page_close_cookie_click_order_from_main_arena_in_main_page(self):
        self.open()
        self.close_cookie()
        self.click_order_from_main_arena_main_page()

    @allure.step("Открыть главную страницу, закрыть куки, в основной части странице на главной странице")
    def open_page_close_cookie_click_order_from_header_main_page(self):
        self.open()
        self.close_cookie()
        self.click_order_from_main_arena_main_page()