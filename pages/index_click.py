from pages.base_page import BasePage
from selenium.webdriver.common.by import By

index_button = (By.CLASS_NAME, '_3bfH1._3qu-v')

class IndexClick(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://dsrny.com/")

    def index(self):
        return self.find(index_button)

    def index_is_click(self):
        return self.index().click()

