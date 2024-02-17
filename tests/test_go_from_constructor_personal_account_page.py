import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver, login
from locators import TestLocators


class TestGetPersonalAccountPage(TestLocators):
    def test_go_from_constructor_to_personal_account_page_positive(self, driver, login):
        # Переход из конструктора в личный кабинет
        """предусловия: авторизация, пользователь находится в конструкторе"""

        """Шаги теста:"""
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be\
                    ('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
