from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.XPATH, "//div[contains(text(), 'Войти')]")
EMAIL_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-wrap')]//div[contains(text(), 'Войти')]")
USER_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
LOGOUT_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]//a[contains(text(), 'Выйти')]")
PROFILE_LOCATOR = (By.XPATH, "//div[contains(@class, 'center-module-centerWrap')]//a[contains(text(), 'Профиль')]")
FULLNAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-contacts-field-name profile__list__row__input')]//input[contains(@class, 'input__inp')]")
PHONE_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-contacts-field-phone profile__list__row__input')]//input[contains(@class, 'input__inp')]")
SAVE_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-footer')]//button[contains(@class, 'button button_submit')]")
