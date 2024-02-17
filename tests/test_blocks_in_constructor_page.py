import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver, email, password
from locators import TestLocators


class TestBlocksInConstructorPage(TestLocators):
    def test_find_sauce_block_positive(self, driver, email, password):
        # Переход в раздел соусов «Конструкторе» с авторизацией
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        driver.find_element(*self.SAUCE_BLOCK).click()
        active_button = driver.find_element(*self.ACTIVE_BUTTON)
        assert active_button.text == "Соусы"

    def test_find_buns_block_positive(self, driver, email, password):
        # Переход в раздел булок «Конструкторе» с авторизацией
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        active_button = driver.find_element(*self.ACTIVE_BUTTON)
        assert active_button.text == "Булки"

    def test_find_filling_block_positive(self, driver, email, password):
        # Переход в раздел начинок в «Конструкторе»
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        driver.find_element(*self.FILLING_BLOCK).click()
        active_button = driver.find_element(*self.ACTIVE_BUTTON)
        assert active_button.text == "Начинки"
