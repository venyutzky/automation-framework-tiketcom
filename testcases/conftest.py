from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['Enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.tiket.com/")
    request.cls.driver = driver
    yield
    driver.close()