import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service)
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()






