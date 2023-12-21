import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPageHelper
from pages.main_page import MainPageHelper
from locators.order_page_locators import OrderPageLocators

"""
Заказ самоката. Нужно проверить весь флоу позитивного сценария с двумя наборами данных. 
Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.
Из чего состоит позитивный сценарий:
Нажать кнопку «Заказать». На странице две кнопки заказа.
Заполнить форму заказа.
Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
Нужно написать тесты с разными данными: минимум два набора. Какие именно данные использовать — на твоё усмотрение.
Сценарий общий, несмотря на разные точки входа: не нужно дважды тестировать каждую из них.
"""


class TestOrderYandexScooter:
    @allure.title(
        "Заказ через клик по кнопке 'Заказать' в шапке страницы, проверить, что появилось всплывающее окно с сообщением об успешном создании заказа")
    @pytest.mark.parametrize("name,second_name,address,phone,times,comment",
                             [('Иван', 'Иванов', 'Московская 5', '89050655488', '25.12.2023', 'Подъезд 5'),],
                             ids=["Positive test1"])
    def test_order_yandex_scooter_via_the_site_header_button(
            self, driver, name, second_name, address, phone, times, comment):
        page = MainPageHelper(driver)
        page.open_page_close_cookie_click_order_from_header_main_page()
        order_page = OrderPageHelper(driver)
        order_page.adding_data_to_fields_who_is_the_scooter_for(name, second_name, address, phone)
        order_page.adding_data_to_about_rent(times, comment)
        order_page.click_order_from_form_order_page()
        order_page.click_button_yes_from_form_want_to_place_an_order_order_page()
        assert "Заказ оформлен" in order_page.wait_for_visibility(
            OrderPageLocators.FORM_ORDER_IS_PROCESSED).text, "Нет текста 'Заказ оформлен'"

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
        order_page.click_order_from_form_order_page()
        order_page.click_button_yes_from_form_want_to_place_an_order_order_page()
        assert "Заказ оформлен" in order_page.wait_for_visibility(
            OrderPageLocators.FORM_ORDER_IS_PROCESSED).text, "Нет текста 'Заказ оформлен'"

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
        # Получаем текущее окно (главную вкладку)
        main_window_handle = driver.current_window_handle
        # Нажимаем на логотип Яндекс, открывая новую вкладку
        order_page.click_logo_yandex()
        # Переключаемся на новую вкладку
        for window_handle in driver.window_handles:
            if window_handle != main_window_handle:
                driver.switch_to.window(window_handle)
        # Теперь мы находимся в новой вкладке, где открыт сайт Яндекс Дзен
        assert "Удобный и быстрый Яндекс Браузер" in order_page.wait_for_visibility(
            OrderPageLocators.YANDEX_DZEN_LOCATOR).text, "Нет текста 'Удобный и быстрый Яндекс Браузер' на сайте Яндекс Дзен"

