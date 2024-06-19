from pages.base_page import BasePage
from selenium.webdriver.common.by import By

index_button = (By.CLASS_NAME, '_3bfH1._3qu-v')

news_article = (By.CSS_SELECTOR, 'a[href="/press-release/columbia-business-school-opens-two-new-buildings-completing-the-first-phase-of-the-university-s-17-acre-manhattanville-campus"]')

class NewsOpen(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://dsrny.com/")

    def index(self):
        return self.find(index_button)

    def index_is_click(self):
        return self.index().click()

    def article(self):
        return self.find(news_article)

    def article_open(self):
        return self.article().click()