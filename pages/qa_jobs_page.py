from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class QAJobsPage(BasePage):
    """Quality Assurance jobs page and embedded job list."""

    URL = "https://useinsider.com/careers/quality-assurance/"

    SEE_ALL_QA_JOBS = (By.XPATH, "//a[contains(., 'See all QA jobs')]")
    FILTER_LOCATION_BUTTON = (By.XPATH, "//button[contains(., 'Location')]")
    FILTER_DEPARTMENT_BUTTON = (By.XPATH, "//button[contains(., 'Department')]")

    OPTION_ISTANBUL = (By.XPATH, "//*[contains(., 'Istanbul, Turkey')]")
    OPTION_QA = (By.XPATH, "//*[contains(., 'Quality Assurance')]")

    JOB_CARD = (By.XPATH, "//div[contains(@class,'position') or contains(@class,'job')]")
    FIELD_POSITION = (By.XPATH, ".//*[self::h3 or self::h2]")
    FIELD_DEPARTMENT = (By.XPATH, ".//*[contains(@class,'department')]")
    FIELD_LOCATION = (By.XPATH, ".//*[contains(@class,'location')]")
    VIEW_ROLE_BTN = (By.XPATH, ".//a[contains(., 'View Role')]")

    def open(self):
        self.driver.get(self.URL)
        self.accept_cookies_if_present()
        return self

    def click_see_all_jobs(self):
        self.click(self.SEE_ALL_QA_JOBS)

    def apply_filters(self):
        self.click(self.FILTER_LOCATION_BUTTON)
        self.click(self.OPTION_ISTANBUL)
        self.click(self.FILTER_DEPARTMENT_BUTTON)
        self.click(self.OPTION_QA)
        # Tüm job kartları görünür olana kadar bekle
        self.wait_all_visible(self.JOB_CARD)

    def get_job_cards(self):
        return self.wait_all_visible(self.JOB_CARD)

    def verify_job_card_fields(self, card) -> bool:
        pos = card.find_element(*self.FIELD_POSITION).text
        dept = card.find_element(*self.FIELD_DEPARTMENT).text
        loc = card.find_element(*self.FIELD_LOCATION).text

        return (
            "Quality Assurance" in pos
            and "Quality Assurance" in dept
            and "Istanbul" in loc
        )

    def open_first_view_role(self, card):
        card.find_element(*self.VIEW_ROLE_BTN).click()
