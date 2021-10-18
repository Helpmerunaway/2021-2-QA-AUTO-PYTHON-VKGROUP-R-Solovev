from base import BaseCase
from ui.locators import basic_locators
import pytest
import time

class TestOne(BaseCase):


    def test_title(self):
        assert "myTarget" in self.driver.title


    def test_login(self):
        login_button = self.find(basic_locators.LOGIN_LOCATOR)
        login_button.click()
        email_button = self.find(basic_locators.EMAIL_LOCATOR)
        email_button.click()
        email_button.send_keys('autotestqa@list.ru')
        password_button = self.find(basic_locators.PASSWORD_LOCATOR)
        password_button.click()
        password_button.send_keys('ThisIsNotAPassword')
        enter_button = self.find(basic_locators.ENTER_LOCATOR)
        enter_button.click()
        assert "AUTOTESTQA@LIST.RU" not in self.driver.page_source
        user_button = self.find(basic_locators.USER_LOCATOR)
        user_button.click()
        time.sleep(2)
        logout_button = self.find(basic_locators.LOGOUT_LOCATOR)
        logout_button.click()
        assert "myTarget" in self.driver.title


    def test_logout(self):
        go_button = self.find(basic_locators.LOGIN_LOCATOR)
        go_button.click()
        login_button = self.find(basic_locators.EMAIL_LOCATOR)
        login_button.click()
        login_button.send_keys('autotestqa@list.ru')
        password_button = self.find(basic_locators.PASSWORD_LOCATOR)
        password_button.click()
        password_button.send_keys('ThisIsNotAPassword')
        enter_button = self.find(basic_locators.ENTER_LOCATOR)
        enter_button.click()
        assert "AUTOTESTQA@LIST.RU" not in self.driver.page_source
        user_button = self.find(basic_locators.USER_LOCATOR)
        user_button.click()
        time.sleep(2)
        logout_button = self.find(basic_locators.LOGOUT_LOCATOR)
        logout_button.click()
        assert "myTarget" in self.driver.title


    def test_change_info(self):
        go_button = self.find(basic_locators.LOGIN_LOCATOR)
        go_button.click()
        login_button = self.find(basic_locators.EMAIL_LOCATOR)
        login_button.click()
        login_button.send_keys('autotestqa@list.ru')
        password_button = self.find(basic_locators.PASSWORD_LOCATOR)
        password_button.click()
        password_button.send_keys('ThisIsNotAPassword')
        enter_button = self.find(basic_locators.ENTER_LOCATOR)
        enter_button.click()
        assert "AUTOTESTQA@LIST.RU" not in self.driver.page_source
        profile_button = self.find(basic_locators.PROFILE_LOCATOR)
        profile_button.click()
        fullname_button = self.find(basic_locators.FULLNAME_LOCATOR)
        fullname_button.click()
        fullname_button.send_keys('Иванов Иван')
        phone_button = self.find(basic_locators.PHONE_LOCATOR)
        phone_button.click()
        phone_button.send_keys('88005553535')
        save_button = self.find(basic_locators.SAVE_LOCATOR)
        save_button.click()
        time.sleep(2)
        user_button = self.find(basic_locators.USER_LOCATOR)
        user_button.click()
        time.sleep(2)
        logout_button = self.find(basic_locators.LOGOUT_LOCATOR)
        logout_button.click()
        assert "myTarget" in self.driver.title


    @pytest.mark.parametrize(" first_page, second_page ", [(«Аудитория», «Баланс»)])
    def test_top_menu_opening_links(first_page, second_page):
        открытие
        страницы
        first_page
        проверка
        что
        открыта
        first_page
        открытие
        страницы
        second_page
        проверка
        что
        открыта
        second_page