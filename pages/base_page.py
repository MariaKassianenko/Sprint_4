import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from variables import timeout_for_webdriverwait as timeout


class BasePage:
    def __init__(self, user):
        self.user = user

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        WebDriverWait(self.user, timeout).until(ec.element_to_be_clickable(locator)).click()

    @allure.step('Считать URL страницы')
    def url_current(self):
        return self.user.current_url

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        button = self.user.find_element(*locator)
        self.user.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Проверить наличие элемента')
    def check_element_presence(self, locator):
        return self.user.find_elements(*locator)

    @allure.step('Переключиться на вторую вкладку, когда она появится в браузере')
    def switch_to_second_tab(self):
        WebDriverWait(self.user, timeout).until_not(ec.number_of_windows_to_be(1))
        second_tab = self.user.window_handles[1]
        self.user.switch_to.window(second_tab)

    @allure.step('Считать текст элемента')
    def get_element_text(self, locator):
        element = WebDriverWait(self.user, timeout).until(ec.visibility_of_element_located(locator))
        return element.text
