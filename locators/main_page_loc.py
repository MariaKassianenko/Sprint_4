from selenium.webdriver.common.by import By


class MainPageLoc:
    order_button_header = (By.XPATH, '//div[contains(@class, "Header")]//button[text()="Заказать"]')
    order_button_finish = (By.XPATH, '//div[contains(@class, "FinishButton")]//button[text()="Заказать"]')
    question_0 = (By.ID, 'accordion__heading-0')
    answer_q0 = (By.XPATH, '//*[@id="accordion__panel-0"]/p')
    question_1 = (By.ID, 'accordion__heading-1')
    answer_q1 = (By.XPATH, '//*[@id="accordion__panel-1"]/p')
    question_2 = (By.ID, 'accordion__heading-2')
    answer_q2 = (By.XPATH, '//*[@id="accordion__panel-2"]/p')
    question_3 = (By.ID, 'accordion__heading-3')
    answer_q3 = (By.XPATH, '//*[@id="accordion__panel-3"]/p')
    question_4 = (By.ID, 'accordion__heading-4')
    answer_q4 = (By.XPATH, '//*[@id="accordion__panel-4"]/p')
    question_5 = (By.ID, 'accordion__heading-5')
    answer_q5 = (By.XPATH, '//*[@id="accordion__panel-5"]/p')
    question_6 = (By.ID, 'accordion__heading-6')
    answer_q6 = (By.XPATH, '//*[@id="accordion__panel-6"]/p')
    question_7 = (By.ID, 'accordion__heading-7')
    answer_q7 = (By.XPATH, '//*[@id="accordion__panel-7"]/p')
