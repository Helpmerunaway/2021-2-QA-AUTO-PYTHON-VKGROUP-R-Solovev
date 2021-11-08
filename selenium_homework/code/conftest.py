import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target.my.com')


@pytest.fixture()
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    return {'browser': browser, 'url': url}


@pytest.fixture(scope='function')
def driver(config):

    browser = config['browser']
    url = config['url']

    if browser == 'chrome':
        browser = webdriver.Chrome(
            executable_path='C:/drivers/chromedriver'
        )
    elif browser == 'firefox':
        browser = webdriver.Firefox(
            executable_path='C:/drivers/geckodriver'
        )
    else:
        raise RuntimeError(f'Unsupported browser: {browser}')

    browser.maximize_window()
    browser.get(url)

    yield browser
    browser.close()