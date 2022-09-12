import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Oc
from selenium.webdriver.firefox.options import Options as Of


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Oc()
        options.add_argument('intl.accept_languages')
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Of()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
