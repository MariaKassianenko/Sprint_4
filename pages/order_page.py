import allure
from pages.base_page import BasePage
from locators.yandex_page_loc import YaPageLoc
from locators.order_page_loc import OrderPageLoc, date_locator
from urls import order_page
import datetime
from random import randint
from variables import timeout_for_webdriverwait as timeout
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OrderPage(BasePage):
    @allure.step('Открыть страницу для оформления заказа')
    def get_order_page(self):
        self.user.get(order_page)
        self.user.find_element(*OrderPageLoc.next_button)

    @allure.step('Заполнить форму заказа')
    def enter_order_data(self, name, last_name, address, underground_st, phone, comment):
        self.user.find_element(*OrderPageLoc.name_field).send_keys(name)
        self.user.find_element(*OrderPageLoc.last_name_field).send_keys(last_name)
        self.user.find_element(*OrderPageLoc.address_field).send_keys(address)
        self.user.find_element(*OrderPageLoc.underground_station_field).send_keys(underground_st)
        station = self.user.find_elements(*OrderPageLoc.underground_search_select)[0]
        WebDriverWait(self.user, timeout).until(ec.element_to_be_clickable(station))
        station.click()
        self.user.find_element(*OrderPageLoc.phone_number_field).send_keys(phone)
        self.user.find_element(*OrderPageLoc.next_button).click()
        order_date = datetime.date.today().day
        self.user.find_element(*OrderPageLoc.when_field).click()
        self.user.find_element(*date_locator(order_date)).click()
        self.user.find_element(*OrderPageLoc.time_field).click()
        order_time_option_to_chose = randint(0, 6)
        self.user.find_element(*OrderPageLoc.time_options[order_time_option_to_chose]).click()
        self.user.find_element(*OrderPageLoc.comment_field).send_keys(comment)
        self.user.find_element(*OrderPageLoc.order_button).click()

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
        WebDriverWait(self.user, timeout).until(ec.visibility_of_element_located(YaPageLoc.ya_search_form))
        return self.user.current_url
