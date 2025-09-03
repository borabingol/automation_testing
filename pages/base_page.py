from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base page object providing common utilities."""

    def __init__(self, driver, timeout: int = 30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Wait helpers ----------
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    # ---------- Element interactions ----------
    def click(self, locator):
        self.wait_clickable(locator).click()

    def type(self, locator, text):
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    # ---------- Cookie banner ----------
    def accept_cookies_if_present(self):
        """Try to accept/close cookie consent banners if present."""
        candidates = [
            (By.ID, "onetrust-accept-btn-handler"),
            (By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"),
            (By.XPATH, "//button[contains(., 'Accept All') or contains(., 'Accept')]"),
        ]
        for by, sel in candidates:
            try:
                self.driver.find_element(by, sel).click()
                return True
            except Exception:
                continue
        return False
