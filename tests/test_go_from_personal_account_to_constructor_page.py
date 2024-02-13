import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from locators import TestLocators


@pytest.mark.parametrize("email, password", [("zarina_sadykova_5_555@yandex.ru", "555zar")])
class TestGetConstructorPage(TestLocators):
    def test_go_from_personal_account_to_constructor_page_by_constructor(self, driver, email, password):
        # Переход из личного кабинета в конструктор - клик на «Конструктор»
        """предусловия: авторизация, пользователь находится в личном кабинете"""
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be\
                    ('https://stellarburgers.nomoreparties.site/account/profile'))
        """Шаги теста:"""
        driver.find_element(*self.TITLE_CONSTRUCTOR).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_go_from_personal_account_to_constructor_page_by_logo(self, driver, email, password):
        # Переход из личного кабинета в конструктор - клик на Logo
        """предусловия: авторизация, пользователь находится в личном кабинете"""
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be\
                    ('https://stellarburgers.nomoreparties.site/account/profile'))
        """Шаги теста:"""
        logo = driver.find_element(*self.LOGO)
        assert logo.is_displayed(), "Элемент не видим"
        logo.click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        # logo = driver.find_element(*self.LOGO)
        # assert logo.is_displayed(), "Элемент не видим"
