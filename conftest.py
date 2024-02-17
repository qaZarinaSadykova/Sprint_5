from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from locators import TestLocators


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # Открываем драйвер перед каждым тестом
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    # Закрываем драйвер после выполнения каждого метода
    driver.quit()


@pytest.fixture
def email():
    email = "zarina_sadykova_5_555@yandex.ru"
    return email


@pytest.fixture
def password():
    password = "555zar"
    return password


@pytest.fixture
def login(driver, email, password):
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT).click()
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
