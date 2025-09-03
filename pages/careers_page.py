from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    """Insider Careers page."""

    LOCATIONS_HDR = (By.XPATH, "//h2[contains(., 'Locations')]")
    TEAMS_HDR = (By.XPATH, "//h2[contains(., 'Teams')]")
    LIFE_HDR = (By.XPATH, "//h2[contains(., 'Life') and contains(., 'Insider')]")

    def blocks_visible(self) -> bool:
        """Return True if all main blocks are visible on the Careers page."""
        try:
            # Tüm blokları bekle
            self.wait_visible(self.LOCATIONS_HDR)
            self.wait_visible(self.TEAMS_HDR)
            self.wait_visible(self.LIFE_HDR)
            return True
        except Exception as e:
            print("Element görünmedi:", e)
            return False
