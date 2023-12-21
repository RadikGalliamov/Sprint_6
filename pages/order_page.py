import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPageHelper(BasePage):
    @allure.step("Заполнение полей формы 'Для кого самокат'")
    def adding_data_to_fields_who_is_the_scooter_for(self, name, second_name, address, phone):
        self.wait_for_clickable(OrderPageLocators.ORDER_FORM_NAME).send_keys(name)
        self.wait_for_clickable(OrderPageLocators.ORDER_FORM_SECOND_NAME).send_keys(second_name)
        self.wait_for_clickable(OrderPageLocators.ORDER_FORM_ADDRESS).send_keys(address)
        self.wait_for_clickable(OrderPageLocators.ORDER_FORM_METRO_STATION).click()
        self.wait_for_clickable(OrderPageLocators.CHOOSE_METRO_STATION).click()
        self.wait_for_clickable(OrderPageLocators.ORDER_FORM_TELEPHONE).send_keys(phone)
        self.wait_for_clickable(OrderPageLocators.BUTTON_FURTHER).click()

    @allure.step("Заполнение полей формы 'Для кого самокат'")
    def adding_data_to_about_rent(self, times, comment):
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_WHEN_TO_DELIVER_THE_ORDER).send_keys(times)
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_WHEN_TO_DELIVER_THE_ORDER_DATA).click()
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_RENTAL_PERIOD).click()
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_RENTAL_PERIOD_LIST).click()
        self.wait_for_clickable(OrderPageLocators.CHECKBOXES_BLACK).click()
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_COMMENT_FOR_THE_COURIER).send_keys(comment)

    @allure.step("Клик по кнопке 'Заказать' формы 'Заказа' на странице заказа")
    def click_order_from_form_order_page(self):
        self.wait_for_clickable(OrderPageLocators.ABOUT_RENT_FORM_BUTTON_ORDER).click()

    @allure.step("Клик по кнопке 'Заказать' в основной части странице на главной странице")
    def click_order_from_header_main_page(self):
        self.wait_for_clickable(MainPageLocators.BUTTON_ORDER_MAIN_AREA).click()

    @allure.step("Клик по кнопке 'Да' формы 'Хотите оформить заказ?' на странице заказа")
    def click_button_yes_from_form_want_to_place_an_order_order_page(self):
        self.wait_for_clickable(OrderPageLocators.BUTTON_YES_WANT_TO_PLACE_AN_ORDER).click()

    @allure.step("Появилась форма 'Заказ оформлен'")
    def visibility_form_order_is_processed(self):
        form_text = self.wait_for_visibility(OrderPageLocators.FORM_ORDER_IS_PROCESSED).text()
        return form_text

    @allure.step("Клик по лого 'Самокат'")
    def click_logo_scooter(self):
        self.wait_for_clickable(OrderPageLocators.LOGO_SCOOTER).click()

    @allure.step("Клик по лого 'Яндекс'")
    def click_logo_yandex(self):
        self.wait_for_clickable(OrderPageLocators.LOGO_YANDEX).click()

    @allure.step("Клик по кнопке 'Посмотреть статус'")
    def click_button_view_status(self):
        self.wait_for_clickable(OrderPageLocators.BUTTON_VIEW_STATUS).click()
