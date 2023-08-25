import allure
from pages.base_page import BasePage
from locators.yandex_page_loc import YaPageLoc
from locators.order_page_loc import OrderPageLoc, date_locator
from urls import order_page
import datetime
from random import randint


class OrderPage(BasePage):
    @allure.step('Открыть страницу для оформления заказа')
    def get_order_page(self):
        self.get_page(order_page)
        self.check_element_presence(OrderPageLoc.next_button)

    @allure.step('Ввести имя в поле "Имя"')
    def fill_name_field(self, name):
        self.send_data_to_input_field(OrderPageLoc.name_field, name)

    @allure.step('Ввести фамилию в поле "Фамилия"')
    def fill_last_name_field(self, last_name):
        self.send_data_to_input_field(OrderPageLoc.last_name_field, last_name)

    @allure.step('Ввести адрес в поле "Адрес"')
    def fill_address_field(self, address):
        self.send_data_to_input_field(OrderPageLoc.address_field, address)

    @allure.step('Заполнить поле "Станция метро"')
    def fill_underground_field(self, underground_st):
        self.send_data_to_input_field(OrderPageLoc.underground_station_field, underground_st)
        station = self.browser.find_elements(*OrderPageLoc.underground_search_select)[0]
        self.click_element (station)

    @allure.step('Ввести номер телефона в поле "Телефон"')
    def fill_phone_field(self, phone):
        self.send_data_to_input_field(OrderPageLoc.phone_number_field, phone)

    @allure.step('Выбрать дату доставки из календаря в поле "Когда привезти самокат"')
    def fill_when_field(self):
        order_date = datetime.date.today().day
        self.click_element(OrderPageLoc.when_field)
        self.click_element(date_locator(order_date))

    @allure.step('Выбрать срок аренды в поле "Срок аренды"')
    def fill_time_field(self):
        self.click_element(OrderPageLoc.time_field)
        order_time_option_to_chose = randint(0, 6)
        self.click_element(OrderPageLoc.time_options[order_time_option_to_chose])

    @allure.step('Выбрать цвет самоката в поле "Цвет самоката"')
    def fill_color_field(self):
        self.click_element(OrderPageLoc.color_field_loc)

    @allure.step('Заполнить поле "Комментарий"')
    def fill_comment_field(self, comment):
        self.send_data_to_input_field(OrderPageLoc.comment_field, comment)

    @allure.step('Заполнить форму заказа')
    def enter_order_data(self, name, last_name, address, underground_st, phone, comment):
        self.fill_name_field(name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.fill_underground_field(underground_st)
        self.fill_phone_field(phone)
        self.click_element(OrderPageLoc.next_button)
        self.fill_when_field()
        self.fill_time_field()
        self.fill_color_field()
        self.fill_comment_field(comment)
        self.click_element(OrderPageLoc.order_button)

    @allure.step('Кликнуть по  кнопке "Да"')
    def click_yes_button(self):
        self.click_element(OrderPageLoc.yes_button)

    @allure.step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_element(OrderPageLoc.scooter_logo)

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(OrderPageLoc.yandex_logo)

    @allure.step('Считать URL страницы после переключения на вторую вкладку')
    def check_yandex_page(self):
        self.switch_to_second_tab()
        self.click_element(YaPageLoc.ya_search_form)
        return self.url_current()
