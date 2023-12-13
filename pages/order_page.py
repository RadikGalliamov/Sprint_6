import allure
import pytest

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPageHelper(BasePage):
    @allure.step("Заполнение полей формы 'Для кого самокат'")
    @pytest.mark.parametrize("name,second_name,address,phone", ['Иван', 'Иванов', 'Московская 5', '89050655488'],
                             ids=["Positive test1"])
    def adding_data_to_fields_who_is_the_scooter_for(self, name, second_name, address, phone):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(*OrderPageLocators.ORDER_FORM_NAME)).click().send_keys(name)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(*OrderPageLocators.ORDER_FORM_SECOND_NAME)).click().send_keys(second_name)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(*OrderPageLocators.ORDER_FORM_ADDRESS)).click().send_keys(address)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_FORM_METRO_STATION)).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.CHOOSE_METRO_STATION)).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(*OrderPageLocators.ORDER_FORM_TELEPHONE)).click().send_keys(phone)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_FURTHER)).click()

    @allure.step("Заполнение полей формы 'Для кого самокат'")
    @pytest.mark.parametrize("time,comment", ['25.12.2023', 'Подъезд 5'], ids=["Positive test1"])
    def adding_data_to_about_rent(self, time, comment):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                OrderPageLocators.ABOUT_RENT_FORM_WHEN_TO_DELIVER_THE_ORDER)).click().send_keys(time)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ABOUT_RENT_FORM_RENTAL_PERIOD)).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ABOUT_RENT_FORM_RENTAL_PERIOD_LIST)).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ABOUT_RENT_FORM_RENTAL_PERIOD)).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                OrderPageLocators.ABOUT_RENT_FORM_COMMENT_FOR_THE_COURIER)).click().send_keys(comment)

    def click_order_from_form_order_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ABOUT_RENT_FORM_BUTTON_ORDER)).click()

    def click_order_from_header_order_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ABOUT_RENT_FORM_BUTTON_ORDER)).click()

    def click_order_from_header_main_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_MAIN_AREA)).click()
