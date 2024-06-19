import time
from selenium.webdriver.common.by import By
from pages.index_click import IndexClick


def test_index_click(browser):
    start_page = IndexClick(browser)
    start_page.open()
    start_page.index_is_click()
    assert 'index' == browser.find_element(By.CSS_SELECTOR,'#dsrMainWrapper > div > div._2vQe4.O9oW9 > a._3bfH1._3qu-v').text
    time.sleep(2)
