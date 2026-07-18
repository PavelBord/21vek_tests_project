from playwright.sync_api import Page, expect
from core.base_page import BasePage
from pages.home_page import HomePage


def test_home_page_url(page: Page):
    base_page = BasePage(page)
    base_page.open("")


def test_search_functional(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.search_catalog_input("холодильник")
    expect(home_page.first_basket_button).to_be_visible()


def test_search_and_add_to_basket(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.search_catalog_input("холодильник")
    expect(home_page.first_basket_button).to_be_visible()
    home_page.click_first_product_basket()
    expect(home_page.basket_counter).to_contain_text("1")
