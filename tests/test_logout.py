import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from locators import TestLocators


@pytest.mark.parametrize("email, password", [("zarina_sadykova_5_555@yandex.ru", "555zar")])
class TestLogout(TestLocators):
    def test_logout_positive(self, driver, email, password):
        # Выход из приложения в личном кабинете
        """предусловия: авторизация, пользователь находится в личном кабинете"""
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be \
                                           ('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.LOGIN_BUTTON))
        start_page = driver.find_element(*self.LOGIN_BUTTON)
        assert start_page.text == "Войти"
