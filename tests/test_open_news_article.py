import time
from pages.news_article import NewsOpen, news_article


def test_open_news_article(browser):
    start_page = NewsOpen(browser)
    start_page.open()
    start_page.index_is_click()
    time.sleep(5)
    start_page.article_open()
    time.sleep(5)
    page_title = browser.title
    assert page_title == 'Columbia Business School Opens Two New Buildings, Completing the First Phase of the University’s 17-Acre Manhattanville Campus - Diller Scofidio + Renfro'
    time.sleep(5)