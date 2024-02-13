from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestBlocksInConstructorPage(TestLocators):
    def test_find_sauce_block_positive(self, driver):
        # Переход в раздел соусов и булок в «Конструкторе»
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*self.SAUCE_BLOCK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.SAUCE_AREA))
        sauce_area = driver.find_elements(*self.SAUCE_AREA)
        assert "Соусы" in sauce_area[0].text
        driver.find_element(*self.BUNS_BLOCK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.BUNS_AREA))
        buns_area = driver.find_elements(*self.BUNS_AREA)
        assert "Булки" in buns_area[0].text

    def test_find_filling_block_positive(self, driver):
        # Переход в раздел начинок в «Конструкторе»
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*self.FILLING_BLOCK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(self.FILLING_AREA))
        filling_area = driver.find_elements(*self.FILLING_AREA)
        assert "Начинки" in filling_area[0].text
