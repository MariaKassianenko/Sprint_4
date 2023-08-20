import allure
import pytest
from locators.order_page_loc import OrderPageLoc
from pages.main_page import MainPage
from pages.order_page import OrderPage
from variables import data_for_order_test
from urls import order_page


class TestScooterOrder:
    @allure.title('Тест функционала заказа самоката')
    @allure.description(
        'Заполнение формы заказа и проверка отображения окна со статусом заказа')
    @pytest.mark.parametrize('name, sec_name, address, metro, phone, comment', data_for_order_test)
    def test_order_scooter(self, user, name, sec_name, address, metro, phone, comment):
        order_page_user = OrderPage(user)
        order_page_user.get_order_page()
        order_page_user.enter_order_data(name, sec_name, address, metro, phone, comment)
        order_page_user.click_yes_button()
        assert order_page_user.check_element_presence(OrderPageLoc.status_button)

    @allure.title('Тест перехода на страницу заказа по кнопке "Заказать" в хедере')
    @allure.description('Проверка входа в форму оформления заказа по кнопке в хэдере основной страницы приложения')
    def test_header_order_button(self, user):
        main_page_user = MainPage(user)
        main_page_user.click_order_button_header()
        order_page_user = OrderPage(user)
        assert order_page_user.url_current() == order_page

    @allure.title('Тест перехода на страницу заказа по кнопку "Заказать" в блоке "как это работает?"')
    @allure.description(
        'Проверка входа в форму оформления заказа по кнопке в блоке "Как это работает?" основной страницы приложения')
    def test_finish_order_button(self, user):
        main_page_user = MainPage(user)
        main_page_user.click_order_button_finish()
        order_page_user = OrderPage(user)
        assert order_page_user.url_current() == order_page
