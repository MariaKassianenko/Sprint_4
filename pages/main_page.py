import allure
from locators.main_page_loc import MainPageLoc
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Отобразить ответ, кликнув по вопросу')
    def get_question_answer(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        self.check_element_presence(answer_locator)

    @allure.step('Кликнуть кнопку "Заказать" в хедере страницы')
    def click_order_button_header(self):
        self.click_element(MainPageLoc.order_button_header)

    @allure.step('Кликнуть кнопку "Заказать" в блоке "Как это работает?"')
    def click_order_button_finish(self):
        self.scroll_to_element(MainPageLoc.order_button_finish)
        self.click_element(MainPageLoc.order_button_finish)
