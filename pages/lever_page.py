from pages.base_page import BasePage


class LeverPage(BasePage):
    """Represents a Lever-hosted job application page."""

    def is_loaded(self) -> bool:
        url = (self.driver.current_url or "").lower()
        return "lever.co" in url
