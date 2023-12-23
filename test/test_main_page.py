import allure
import pytest

from pages.main_page import MainPageHelper
from locators.main_page_locators import MainPageLocators


class TestSectionQuestionsAboutImportant:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY,
         MainPageLocators.TEXT_HOW_MUCH_DOES_IT_COST_AND_HOW_TO_PAY,
         "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (MainPageLocators.I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE,
         MainPageLocators.TEXT_I_WANT_SEVERAL_SCOOTER_AT_ONCE_SO_IT_IS_POSSIBLE,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (MainPageLocators.HOW_IS_RENTAL_TIME_CALCULATED,
         MainPageLocators.TEXT_HOW_IS_RENTAL_TIME_CALCULATED,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (MainPageLocators.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY,
         MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_TODAY,
         "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (MainPageLocators.IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER,
         MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER,
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (MainPageLocators.DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER,
         MainPageLocators.TEXT_DO_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER,
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (MainPageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER,
         MainPageLocators.TEXT_IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER,
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (MainPageLocators.I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT,
         MainPageLocators.TEXT_I_LIVE_OUTSIDE_THE_MRR_CAN_YOU_BRING_IT,
         "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ], ids=[
        "how_much_does_it_cost_and_how_to_pay?",
        "i_want_several_scooter_at_once_so_it_is_possible?",
        "how_is_rental_time_calculated?",
        "is_it_possible_to_order_a_scooter_today?",
        "is_it_possible_to_extend_the_order_or_return_the_scooter_earlier?",
        "do_you_bring_the_charger_along_with_the_scooter?",
        "is_it_possible_to_cancel_an_order?",
        "i_live_outside_the_mrr_can_you_bring_it?"
    ])
    @allure.title("Тест выпадающий список Вопросы о важном")
    def test_questions_about_important(self, driver, question_locator, answer_locator, expected_text):
        page = MainPageHelper(driver)
        page.open()
        page.close_cookie()
        page.scroll_text_questions_about_important_things()
        page.wait_and_click(question_locator)
        text = page.get_text(answer_locator)
        assert text == expected_text

