import allure
import pytest

from pages.order_page import OrderPageHelper
from pages.main_page import MainPageHelper


class TestOrderYandexScooter:
    @allure.title(
        "Заказ через клик по кнопке 'Заказать' в шапке страницы, проверить, что появилось всплывающее окно с сообщением об успешном создании заказа")
    @pytest.mark.parametrize("name,second_name,address,phone,times,comment",
                             [('Иван', 'Иванов', 'Московская 5', '89050655488', '25.12.2023', 'Подъезд 5'), ],
                             ids=["Positive test"])
    def test_order_yandex_scooter_via_the_site_header_button(
            self, driver, name, second_name, address, phone, times, comment):
        page = MainPageHelper(driver)
        page.open_page_close_cookie_click_order_from_header_main_page()
        order_page = OrderPageHelper(driver)
        order_page.adding_data_to_fields_who_is_the_scooter_for(name, second_name, address, phone)
        order_page.adding_data_to_about_rent(times, comment)
        assert order_page.is_order_confirmation_message_displayed(), "Текст 'Заказ оформлен' не найден"

    @allure.title(
        "Заказ через клик по кнопке 'Заказать' в основной части страницы, что появилось всплывающее окно с сообщением об успешном создании заказа")
    @pytest.mark.parametrize("name,second_name,address,phone,times,comment",
                             [('Иван', 'Иванов', 'Московская 5', '89050655488', '25.12.2023', 'Подъезд 5')],
                             ids=["Positive test"])
    def test_order_yandex_scooter_via_the_site_main_area_button(
            self, driver, name, second_name, address, phone, times, comment):
        page = MainPageHelper(driver)
        page.open_page_close_cookie_click_order_from_main_arena_in_main_page()
        order_page = OrderPageHelper(driver)
        order_page.adding_data_to_fields_who_is_the_scooter_for(name, second_name, address, phone)
        order_page.adding_data_to_about_rent(times, comment)
        assert order_page.is_order_confirmation_message_displayed(), "Текст 'Заказ оформлен' не найден"

