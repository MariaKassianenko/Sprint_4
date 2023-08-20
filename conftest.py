import pytest
from selenium import webdriver
from urls import main_page


@pytest.fixture
def user():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(main_page)
    yield browser
    browser.quit()
