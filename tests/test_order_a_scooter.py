import allure
import pytest
from locators.order_page_loc import OrderPageLoc
from pages.main_page import MainPage
from pages.order_page import OrderPage
from variables import data_for_order_test
from urls import order_page


@allure.feature('Функционал заказа самоката')
class TestScooterOrder:
    @allure.title('Тест функционала заказа самоката')
    @allure.description(
        'Заполнение формы заказа и проверка отображения окна со статусом заказа')
    @pytest.mark.parametrize('name, sec_name, address, metro, phone, comment', data_for_order_test)
    def test_order_scooter(self, browser, name, sec_name, address, metro, phone, comment):
        order_page_browser = OrderPage(browser)
        order_page_browser.get_order_page()
        order_page_browser.enter_order_data(name, sec_name, address, metro, phone, comment)
        order_page_browser.click_yes_button()
        assert order_page_browser.check_element_presence(OrderPageLoc.status_button), \
            'Заказ не оформлен, на экране не отобразилась кнопка "Посмотреть статус"'

    @allure.title('Тест перехода на страницу заказа по кнопке "Заказать" в хедере')
    @allure.description('Проверка входа в форму оформления заказа по кнопке в хэдере основной страницы приложения')
    def test_header_order_button(self, browser):
        main_page_browser = MainPage(browser)
        main_page_browser.click_order_button_header()
        order_page_browser = OrderPage(browser)
        result_page = order_page_browser.url_current()
        assert result_page == order_page, \
            f'Переход на ожидаемую страницу {order_page} не происходит. Отображается {result_page}'

    @allure.title('Тест перехода на страницу заказа по кнопку "Заказать" в блоке "как это работает?"')
    @allure.description(
        'Проверка входа в форму оформления заказа по кнопке в блоке "Как это работает?" основной страницы приложения')
    def test_finish_order_button(self, browser):
        main_page_user = MainPage(browser)
        main_page_user.click_order_button_finish()
        order_page_user = OrderPage(browser)
        result_page = order_page_user.url_current()
        assert result_page == order_page, \
            f'Переход на ожидаемую страницу {order_page} не происходит. Отображается {result_page}'
