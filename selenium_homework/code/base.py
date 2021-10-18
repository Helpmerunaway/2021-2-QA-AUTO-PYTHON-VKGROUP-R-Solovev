import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

CLICK_RETRY = 3


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    #def find(self, locator):
        #print(self.driver.find_element(*locator))

        #return self.driver.find_element(*locator)

    def find(self, locator, time=5):
        """
        Нахождение элементов
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    #def search(self, query):
        #search = self.find(basic_locators.QUERY_LOCATOR)
        #search.send_keys(query)
        #go_button = self.find(basic_locators.GO_LOCATOR)
        #time.sleep(5)
        #go_button.click()

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