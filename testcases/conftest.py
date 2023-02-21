from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#To run
## pytest -v --browser chrome --url https://www.tiket.com/

@pytest.fixture(autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['Enable-logging'])
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_experimental_option('excludeSwitches', ['Enable-logging'])
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['Enable-logging'])
        driver  = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()
    
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)    
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)    
def url(request):
    return request.config.getoption("--url")
    