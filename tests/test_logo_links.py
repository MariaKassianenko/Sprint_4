import allure
from pages.order_page import OrderPage
from urls import yandex_page, main_page


class TestButtons:
    @allure.title('Тест перехода на главную странцие приложения по клику на логотип Самокат')
    @allure.description(
        'Проверка перехода на главную страницу прилоджения по нажатию на логотип приложения в '
        'хэдере страницы оформления заказа')
    def test_scooter_logo_link(self, user):
        order_page_user = OrderPage(user)
        order_page_user.get_order_page()
        order_page_user.click_scooter_logo()
        assert order_page_user.url_current() == main_page

    @allure.title('Тест перехода на главную странцие Яндекса по клику на логотип Яндекса')
    @allure.description(
        'Проверка перехода на главную страницу Яндекса по нажатию на логотип Яндекса '
        'в хэдере страницы оформления заказа в приложении')
    def test_yandex_logo_link(self, user):
        order_page_user = OrderPage(user)
        order_page_user.get_order_page()
        order_page_user.click_yandex_logo()
        assert order_page_user.check_yandex_page() == yandex_page
