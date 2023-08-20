import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_loc import MainPageLoc
from variables import correct_answers as ca


class TestMainPageQuestions:
    @allure.title('Тест ответов на вопросы на главной странице')
    @allure.description(
        'Проверка соответствия ответов на вопросы на главной странице ожидаемому тексту')
    @pytest.mark.parametrize('question_locator, answer_locator, correct_answer_to_question', (
        (MainPageLoc.question_0, MainPageLoc.answer_q0, ca.get('correct_answer_q0')),
        (MainPageLoc.question_1, MainPageLoc.answer_q1, ca.get('correct_answer_q1')),
        (MainPageLoc.question_2, MainPageLoc.answer_q2, ca.get('correct_answer_q2')),
        (MainPageLoc.question_3, MainPageLoc.answer_q3, ca.get('correct_answer_q3')),
        (MainPageLoc.question_4, MainPageLoc.answer_q4, ca.get('correct_answer_q4')),
        (MainPageLoc.question_5, MainPageLoc.answer_q5, ca.get('correct_answer_q5')),
        (MainPageLoc.question_6, MainPageLoc.answer_q6, ca.get('correct_answer_q6')),
        (MainPageLoc.question_7, MainPageLoc.answer_q7, ca.get('correct_answer_q7'))
    ))
    def test_main_page_answers_to_questions(self, user, question_locator, answer_locator, correct_answer_to_question):
        main_page_user = MainPage(user)
        main_page_user.get_question_answer(question_locator, answer_locator)
        assert main_page_user.get_element_text(answer_locator) == correct_answer_to_question
