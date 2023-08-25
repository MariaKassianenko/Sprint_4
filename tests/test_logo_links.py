import allure
from pages.order_page import OrderPage
from urls import yandex_page, main_page


@allure.feature('Переходы по логотипам в шапке приложения')
class TestButtons:
    @allure.title('Тест перехода на главную странцие приложения по клику на логотип Самокат')
    @allure.description(
        'Проверка перехода на главную страницу прилоджения по нажатию на логотип приложения в '
        'хэдере страницы оформления заказа')
    def test_scooter_logo_link(self, browser):
        order_page_browser = OrderPage(browser)
        order_page_browser.get_order_page()
        order_page_browser.click_scooter_logo()
        result_page = order_page_browser.url_current()
        assert result_page == main_page, \
            f'Переход на ожидаемую страницу {main_page} не происходит. Отображается {result_page}'

    @allure.title('Тест перехода на главную странцие Яндекса по клику на логотип Яндекса')
    @allure.description(
        'Проверка перехода на главную страницу Яндекса по нажатию на логотип Яндекса '
        'в хэдере страницы оформления заказа в приложении')
    def test_yandex_logo_link(self, browser):
        order_page_browser = OrderPage(browser)
        order_page_browser.get_order_page()
        order_page_browser.click_yandex_logo()
        result_page = order_page_browser.check_yandex_page()
        assert result_page == yandex_page, \
            f'Переход на ожидаемую страницу {yandex_page} не происходит. Отображается {result_page}'
