import allure
import pytest
import time
from pages.main_page import MainPageHelper
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

"""
Выпадающий список в разделе «Вопросы о важном». 
Тебе нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст. 
Важно написать отдельный тест на каждый вопрос
"""


class TestSectionQuestionsAboutImportant:
    @allure.story
    @allure.feature
    @allure.step("Тест какой-то")
    def test_how_much_does_it(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.TEXT_HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY)).text
        assert text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.step("Тест какой-то")
    def test_how_much_does_it2(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE)).text
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it3(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.HOW_IS_RENTAL_TIME_CALCULATED)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_HOW_IS_RENTAL_TIME_CALCULATED)).text
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it4(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                MainPageLocators.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY)).text
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it5(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER)).text
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it6(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                MainPageLocators.DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER)).text
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it7(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER)).text
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert text == expected_text

    @allure.step("Тест какой-то")
    def test_how_much_does_it8(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT)).click()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.TEXT_I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT)).text
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        assert text == expected_text     
            
            
    

