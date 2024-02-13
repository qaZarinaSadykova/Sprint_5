from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # Открываем драйвер перед каждым тестом
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    # Закрываем драйвер после выполнения каждого метода
    driver.quit()


