import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver, login
from locators import TestLocators


class TestGetConstructorPage(TestLocators):
    def test_go_from_personal_account_to_constructor_page_by_constructor(self, driver, login):
        # Переход из личного кабинета в конструктор - клик на «Конструктор»
        """предусловия: авторизация, пользователь находится в личном кабинете"""
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be\
                    ('https://stellarburgers.nomoreparties.site/account/profile'))
        """Шаги теста:"""
        driver.find_element(*self.TITLE_CONSTRUCTOR).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_go_from_personal_account_to_constructor_page_by_logo(self, driver, login):
        # Переход из личного кабинета в конструктор - клик на Logo
        """предусловия: авторизация, пользователь находится в личном кабинете"""
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be\
                    ('https://stellarburgers.nomoreparties.site/account/profile'))
        logo = driver.find_element(*self.LOGO)
        logo.click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
