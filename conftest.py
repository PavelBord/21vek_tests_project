import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.fixture
def home_page(page:Page) -> HomePage:
    custom_home = HomePage(page)
    custom_home.open()
    return custom_home
