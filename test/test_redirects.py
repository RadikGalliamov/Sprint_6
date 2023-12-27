import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPageHelper
from pages.main_page import MainPageHelper


class TestRedirectForYandex:
    @allure.title("Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».")
    @pytest.mark.parametrize("name,second_name,address,phone,times,comment",
                             [('Иван', 'Иванов', 'Московская 5', '89050655488', '25.12.2023', 'Подъезд 5')],
                             ids=["Positive test"])
    def test_click_on_the_scooter_logo_redirect_to_main_page(
            self, driver, name, second_name, address, phone, times, comment):
        page = MainPageHelper(driver)
        page.open_page_close_cookie_click_order_from_header_main_page()
        order_page = OrderPageHelper(driver)
        order_page.adding_data_to_fields_who_is_the_scooter_for(name, second_name, address, phone)
        order_page.adding_data_to_about_rent(times, comment)
        order_page.click_order_from_form_order_page()
        order_page.click_button_yes_from_form_want_to_place_an_order_order_page()
        order_page.click_button_view_status()
        order_page.click_logo_scooter()
        page.scroll_text_questions_about_important_things()
        text = page.get_text(MainPageLocators.TEXT_QUESTIONS_ABOUT_IMPORTANT_THINGS)
        assert text == "Вопросы о важном", "Нет текста 'Вопросы о важном' на главной странице Яндекс Самокат"

    @allure.title("Проверить: если нажать на логотип Яндекса, "
                  "в новом окне через редирект откроется главная страница Дзена.")
    @pytest.mark.parametrize("name,second_name,address,phone,times,comment",
                             [('Иван', 'Иванов', 'Московская 5', '89050655488', '25.12.2023', 'Подъезд 5')],
                             ids=["Positive test"])
    def test_click_scooter_yandex_logo_will_be_new_windows_with_main_page_yandex(
            self, driver, name, second_name, address, phone, times, comment):
        page = MainPageHelper(driver)
        page.open_page_close_cookie_click_order_from_header_main_page()
        order_page = OrderPageHelper(driver)
        order_page.adding_data_to_fields_who_is_the_scooter_for(name, second_name, address, phone)
        order_page.adding_data_to_about_rent(times, comment)
        order_page.click_order_from_form_order_page()
        order_page.click_button_yes_from_form_want_to_place_an_order_order_page()
        order_page.click_button_view_status()
        # Нажимаем на логотип Яндекс, открывая новую вкладку
        order_page.click_logo_yandex()
        # Переключаемся на новую вкладку
        order_page.switch_to_new_tab()
        assert order_page.check_yandex_dzen_text(), "Нет текста 'Удобный и быстрый Яндекс Браузер' на сайте Яндекс Дзен"
