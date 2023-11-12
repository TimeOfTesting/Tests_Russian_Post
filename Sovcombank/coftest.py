import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def setup_teardown(request, driver):
    driver.save_state = driver.get_window_rect()

    def teardown():
        driver.set_window_rect(**driver.save_state)

    request.addfinalizer(teardown)

