import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    timeout = 5

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Загрузить страницу')
    def get_page(self, url):
        self.browser.get(url)

    @allure.step('Ввести данные в поле ввода')
    def send_data_to_input_field(self, input_locator, data):
        WebDriverWait(self.browser, self.timeout).until(ec.presence_of_element_located(input_locator))
        self.browser.find_element(*input_locator).send_keys(data)

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        WebDriverWait(self.browser, self.timeout).until(ec.element_to_be_clickable(locator)).click()

    @allure.step('Считать URL страницы')
    def url_current(self):
        return self.browser.current_url

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        button = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Проверить наличие элемента')
    def check_element_presence(self, locator):
        return self.browser.find_elements(*locator)

    @allure.step('Переключиться на вторую вкладку, когда она появится в браузере')
    def switch_to_second_tab(self):
        WebDriverWait(self.browser, self.timeout).until_not(ec.number_of_windows_to_be(1))
        second_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(second_tab)

    @allure.step('Считать текст элемента')
    def get_element_text(self, locator):
        element = WebDriverWait(self.browser, self.timeout).until(ec.visibility_of_element_located(locator))
        return element.text
