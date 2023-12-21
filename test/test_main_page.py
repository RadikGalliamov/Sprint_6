import allure
from pages.main_page import MainPageHelper
from locators.main_page_locators import MainPageLocators

"""
Выпадающий список в разделе «Вопросы о важном». 
Тебе нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст. 
Важно написать отдельный тест на каждый вопрос
"""


class TestSectionQuestionsAboutImportant:

    @allure.title("Тест выпадающий список Вопросы о важном 'Сколько это стоит? И как оплатить?'")
    def test_how_much_does_it_cost_and_how_to_pay(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_for_clickable(MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY)
        text = page.get_text(MainPageLocators.TEXT_HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY)
        assert text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title("Тест выпадающий список Вопросы о важном 'Хочу сразу несколько самокатов! Так можно?'")
    def test_i_want_several_scooter_at_once_so_it_is_possible(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE)
        text = page.get_text(MainPageLocators.TEXT_I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE)
        assert text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title("Тест выпадающий список Вопросы о важном 'Как рассчитывается время аренды?'")
    def test_how_is_rental_time_calculated(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.HOW_IS_RENTAL_TIME_CALCULATED)
        text = page.get_text(MainPageLocators.TEXT_HOW_IS_RENTAL_TIME_CALCULATED)
        assert text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title("Тест выпадающий список Вопросы о важном 'Можно ли заказать самокат прямо на сегодня?'")
    def test_is_it_possible_to_order_a_scooter_today(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY)
        text = page.get_text(MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY)
        assert text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title("Тест выпадающий список Вопросы о важном 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER)
        text = page.get_text(MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER)
        assert text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title("Тест выпадающий список Вопросы о важном 'Вы привозите зарядку вместе с самокатом?'")
    def test_do_you_bring_the_charger_along_with_the_scooter(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER)
        text = page.get_text(MainPageLocators.TEXT_DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER)
        assert text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title("Тест выпадающий список Вопросы о важном 'Можно ли отменить заказ?'")
    def test_is_it_possible_to_cancel_an_order(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER)
        text = page.get_text(MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER)
        assert text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title("Тест выпадающий список Вопросы о важном 'Я живу за МКАДом, привезёте?'")
    def test_i_live_outside_the_mrr_can_you_bring_it(self, driver):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(MainPageLocators.I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT)
        text = page.get_text(MainPageLocators.TEXT_I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT)
        assert text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
