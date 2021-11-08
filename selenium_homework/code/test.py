from base import BaseCase
from ui.locators import basic_locators
import pytest

class TestOne(BaseCase):


    def test_title(self):
        assert "myTarget" in self.driver.title

    @pytest.mark.UI
    def test_login(self):
        self.find(basic_locators.LOGIN_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).send_keys('autotestqa@list.ru')
        self.find(basic_locators.PASSWORD_LOCATOR).click()
        self.find(basic_locators.PASSWORD_LOCATOR).send_keys('ThisIsNotAPassword')
        self.find(basic_locators.ENTER_LOCATOR).click()
        assert "ПРОФИЛЬ" not in self.driver.page_source

    @pytest.mark.UI
    def test_logout(self):
        self.find(basic_locators.LOGIN_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).send_keys('autotestqa@list.ru')
        self.find(basic_locators.PASSWORD_LOCATOR).click()
        self.find(basic_locators.PASSWORD_LOCATOR).send_keys('ThisIsNotAPassword')
        self.find(basic_locators.ENTER_LOCATOR).click()
        assert "ПРОФИЛЬ" not in self.driver.page_source
        self.find(basic_locators.USER_LOCATOR).click()
        self.find(basic_locators.LOGOUT_LOCATOR).click()
        assert "myTarget" in self.driver.title

    @pytest.mark.UI
    def test_change_info(self):
        self.find(basic_locators.LOGIN_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).click()
        self.find(basic_locators.EMAIL_LOCATOR).send_keys('autotestqa@list.ru')
        self.find(basic_locators.PASSWORD_LOCATOR).click()
        self.find(basic_locators.PASSWORD_LOCATOR).send_keys('ThisIsNotAPassword')
        self.find(basic_locators.ENTER_LOCATOR).click()
        assert "ПРОФИЛЬ" not in self.driver.page_source
        self.find(basic_locators.PROFILE_LOCATOR).click()
        self.find(basic_locators.FULLNAME_LOCATOR).click()
        self.find(basic_locators.FULLNAME_LOCATOR).send_keys('Иванов Иван')
        self.find(basic_locators.PHONE_LOCATOR).click()
        self.find(basic_locators.PHONE_LOCATOR).send_keys('88005553535')
        self.find(basic_locators.SAVE_LOCATOR).click()
        self.find(basic_locators.USER_LOCATOR).click()
        self.find(basic_locators.LOGOUT_LOCATOR).click()
        assert "myTarget" in self.driver.title




