import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPageHelper(BasePage):
    @allure.step("Тест какой-то")
    def enter_in_section(self):
        pass

    # Метод проверки на корректный url адрес (подстрока "login" есть в текущем url браузере)
    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, 'Ссылка не содержит слово "login"'

    def scroll_text_questions_about_important_things(self):
        element = self.driver.find_element(*MainPageLocators.TEXT_QUESTIONS_ABOUT_IMPORTANT_THINGS)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_clickable(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY)).click()

    def click_order_from_header_main_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_HEADER)).click()

    def click_order_from_main_arena_main_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_MAIN_AREA)).click()
