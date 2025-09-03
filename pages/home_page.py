from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
import time

class HomePage(BasePage):
    """Insider Home Page object."""

    URL = "https://useinsider.com/"

    NAV_COMPANY = (By.XPATH, "//nav//a[contains(., 'Company')]")
    NAV_CAREERS = (By.XPATH, "//nav//a[contains(., 'Careers')]")
    HERO_ANY = (By.CSS_SELECTOR, "main, section, header")

    def open(self):
        self.driver.get(self.URL)
        self.accept_cookies_if_present()
        return self

    def is_loaded(self) -> bool:
        hero_visible = self.is_visible(self.HERO_ANY)
        title_ok = "Insider" in (self.driver.title or "")
        return hero_visible and title_ok

    def go_to_careers(self):
        company_menu = self.wait_visible(self.NAV_COMPANY)
        ActionChains(self.driver).move_to_element(company_menu).perform()
        # Dropdown açıldıktan sonra "Careers" tıklanabilir olana kadar bekle
        self.wait_clickable(self.NAV_CAREERS)
        self.click(self.NAV_CAREERS)