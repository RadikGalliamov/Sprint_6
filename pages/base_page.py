import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators  import MainPageLocators
from data import ConstantData


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ConstantData.MAIN_URL

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Закрыть куки")
    def close_cookie(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)).click()

    @allure.step("Найти элемент")
    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_element_located(locator),
                   message=f"Не найден элемент = {locator}")
