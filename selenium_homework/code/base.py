import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY = 3


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator, wait=3):
        """
        Нахождение элементов
        """
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def clicks(self, locator):
        elem = self.driver.find_element(*locator)
        self.driver.refresh()
        elem.click()

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                if i < 2:
                    self.driver.refresh()
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise