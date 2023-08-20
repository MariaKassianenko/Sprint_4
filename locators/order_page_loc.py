from selenium.webdriver.common.by import By


class OrderPageLoc:
    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    last_name_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    underground_station_field = (By.XPATH,  '//input[@placeholder="* Станция метро"]')
    phone_number_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    underground_search_select = (By.XPATH, '//div[@class="select-search__select"]/*')
    next_button = (By.XPATH, '//button[contains(text(),"Далее")]')
    when_field = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    time_field = (By.XPATH, '//div[contains(text(),"* Срок аренды")]')
    comment_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    time_options = (
        (By.XPATH, '//div[contains(text(),"сутки")]'),
        (By.XPATH, '//div[contains(text(),"двое суток")]'),
        (By.XPATH, '//div[contains(text(),"трое суток")]'),
        (By.XPATH, '//div[contains(text(),"четверо суток"")]'),
        (By.XPATH, '//div[contains(text(),"пятеро суток")]'),
        (By.XPATH, '//div[contains(text(),"шестеро суток")]'),
        (By.XPATH, '//div[contains(text(),"семеро суток")]')
    )
    order_button = (By.XPATH, '//div[contains(@class, "Order")]/button[contains(text(),"Заказать")]')
    yes_button = (By.XPATH, '//button[contains(text(),"Да")]')
    status_button = (By.XPATH, '//button[contains(text(),"Посмотреть статус")]')


def date_locator(day):
    return By.XPATH, f'//*[@class="react-datepicker"]//*[text()="{day}"]'
