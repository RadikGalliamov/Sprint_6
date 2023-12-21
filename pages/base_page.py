import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from data import ConstantData


class BasePage:
    @allure.step('Инициируем создание объекта класса BasePage')
    def __init__(self, driver):
        """
        Конструктор класса BasePage.
        :param driver: Экземпляр драйвера, который будет использоваться для взаимодействия с веб-страницей.
        """
        self.driver = driver
        self.base_url = ConstantData.MAIN_URL  # Базовый URL для построения полных URL страниц

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Закрыть куки")
    def close_cookie(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)).click()

    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_element_located(locator),
                   message=f"Не найден элемент = {locator}")

    @allure.step("Выполнить JavaScript-скрипт")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Скроллинг до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание и клик по элементу")
    def wait_and_click(self, locator, wait_time=10):
        element = self.find_element(locator, wait_time)
        element.click()

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}")
        return element

    @allure.step("Ожидание кликабельного элемента")
    def wait_for_clickable(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}"
        )
        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не стал кликабельным: {locator}"
        )
        return element

    @allure.step("Получение текста элемента")
    def get_text(self, locator, wait_time=10):
        element = self.wait_for_visibility(locator, wait_time)
        return element.text
