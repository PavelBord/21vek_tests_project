from playwright.sync_api import Page, Locator
from core.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.button_module: Locator = page.locator("[class*='Button-module__button']")
        self.search_input: Locator = page.locator("#catalogSearch:visible")
        self.basket_counter: Locator = page.locator("header a[href*='/order/']").first
        self.first_basket_button: Locator = page.get_by_test_id("card-basket-action").first
        self.promo_popup_close: Locator = page.locator("[data-popmechanic-close]").first


    def open(self) -> None:
        super().open("")

    def click_first_product_basket(self) -> None:
        self.first_basket_button.scroll_into_view_if_needed()
        self.first_basket_button.click()

    def search_catalog_input(self, product_name: str) -> None:
        self.search_input.fill(product_name)
        self.search_input.press("Enter")
        self.promo_popup_close.dispatch_event("click")
        self.first_basket_button.wait_for(state="visible")
        self.clear_all_popups()

    def click_button_by_text(self) -> None:
        self.first_basket_button.scroll_into_view_if_needed()
        self.first_basket_button.click()
        self.clear_all_popups()
