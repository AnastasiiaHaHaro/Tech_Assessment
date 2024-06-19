import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service)
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()






