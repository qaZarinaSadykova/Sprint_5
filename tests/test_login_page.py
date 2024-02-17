
from conftest import driver, email, password
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestLoginPage(TestLocators):
    def test_login_general_form_positive(self, driver, email, password):
        # Авторизация по кнопке - Войти в аккаунт
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        order_button = driver.find_element(*self.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    def test_login_in_personal_account_positive(self, driver, email, password):
        # Авторизация по кнопке  - Личный кабинет
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        order_button = driver.find_element(*self.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    def test_login_in_registration_form_positive(self, driver, email, password):
        # Авторизация в форме регистрации  - Войти
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()
        registration_button = driver.find_element(*self.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", registration_button)
        registration_button.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.REGISTRATION_SUBMIT))
        driver.find_element(*self.LOGIN_FROM_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.LOGIN_BUTTON))
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        order_button = driver.find_element(*self.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    def test_login_in_restore_password_form_positive(self, driver, email, password):
        # Авторизация в форме восстановить пароль - Войти
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        restore_password_button = driver.find_element(*self.RESTORE_PASSWORD_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", restore_password_button)
        restore_password_button.click()
        driver.find_element(*self.LOGIN_FROM_RESET_PASSWORD).click()
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        order_button = driver.find_element(*self.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
