
import random

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver


class TestRegistration(TestLocators):
    def test_registration_new_user_positive(self, driver):
        email = f'zarina_sadykova{random.randint(100, 999)}@yandex.ru'
        password = f'{random.randint(100, 999999)}zar'
        # Регистрация нового пользователя c успешной авторизацией
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        registration_button = driver.find_element(*self.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", registration_button)
        registration_button.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.REGISTRATION_SUBMIT))
        driver.find_element(*self.NAME_INPUT).send_keys("Zarina")
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.LOGIN_BUTTON))
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        order_button = driver.find_element(*self.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    def test_registration_with_old_user_data_error_message(self, driver):
        # Регистрация нового пользователя c существующими данными - ошибка "Такой пользователь уже существует"
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        registration_button = driver.find_element(*self.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", registration_button)
        registration_button.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.REGISTRATION_SUBMIT))
        driver.find_element(*self.NAME_INPUT).send_keys("Zarina")
        driver.find_element(*self.EMAIL_INPUT).send_keys("zarina_sadykova_5_555.yandex.ru")
        driver.find_element(*self.PASSWORD_INPUT).send_keys("555zar")
        driver.find_element(*self.REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.USER_EXISTS_MESSAGE))
        error_message = driver.find_element(*self.USER_EXISTS_MESSAGE)
        assert error_message.text == "Такой пользователь уже существует", "Нет сообщения об ошибке"

    @pytest.mark.parametrize("password", ["12345", " ", 0])
    def test_registration_new_user_with_incorrect_password_error_message(self, driver, password):
        email = f'zarina_sadykova{random.randint(100, 999)}@yandex.ru'
        # Регистрация нового пользователя с неверным паролем  - ошибка "Некорректный пароль"
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        registration_button = driver.find_element(*self.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", registration_button)
        registration_button.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.REGISTRATION_SUBMIT))
        driver.find_element(*self.NAME_INPUT).send_keys("Zarina")
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.REGISTRATION_SUBMIT).click()
        error_password = driver.find_element(*self.INCORRECT_PASSWORD_MESSAGE)
        assert error_password.text == "Некорректный пароль", "Нет сообщения об ошибке"
