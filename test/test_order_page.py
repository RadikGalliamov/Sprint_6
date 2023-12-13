import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.order_page import OrderPageHelper
from pages.main_page import MainPageHelper

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
    # @allure.story
    # @allure.feature
    # @allure.step("Тест заказа самоката")
    # @pytest.mark.parametrize
    def test_order_yandex_scooter(self, driver):
        page = OrderPageHelper(driver)
        page.open()
        page.close_cookie()
        page.click_order_from_header_main_page()
        page.adding_data_to_fields_who_is_the_scooter_for()
        page.adding_data_to_about_rent()
