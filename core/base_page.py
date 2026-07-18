from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.accept_cookies_button: Locator = page.locator("button:has-text('Принять'):visible")
        self.currency_ok_button: Locator = page.locator(".Button-module__buttonText:visible", has_text="Понятно")

    def open(self, path: str) -> None:
        self.page.route("**/popmechanic**", lambda route: route.abort())
        self.page.goto(path)
        self.clear_all_popups()

    def clear_all_popups(self) -> None:
        self.page.wait_for_timeout(500)
        popus = [self.accept_cookies_button, self.currency_ok_button]
        for locator in popus:
            for button in locator.all():
                button.click(force=True)
