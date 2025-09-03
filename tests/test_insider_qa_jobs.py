from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from pages.lever_page import LeverPage

# ---------- Test 1: Home page ----------
def test_home_page_loads(driver, base_url):
    home = HomePage(driver).open()
    assert home.is_loaded(), "Home page did not load as expected"

# ---------- Test 2: Careers page ----------
def test_careers_blocks_visible(driver, base_url):
    home = HomePage(driver).open()
    home.go_to_careers()
    careers = CareersPage(driver)
    assert careers.blocks_visible(), "Careers blocks not visible"

# ---------- Test 3: QA jobs page ----------
def test_qa_jobs_list(driver, qa_url):
    qa = QAJobsPage(driver).open()
    qa.click_see_all_jobs()
    qa.apply_filters()
    cards = qa.get_job_cards()
    assert len(cards) > 0, "Filtered job list is empty"
    for idx, card in enumerate(cards, start=1):
        assert qa.verify_job_card_fields(card), f"Job card #{idx} is invalid"

# ---------- Test 4: QA job View Role ----------
def test_qa_job_view_role(driver, qa_url):
    qa = QAJobsPage(driver).open()
    qa.click_see_all_jobs()
    qa.apply_filters()
    cards = qa.get_job_cards()
    qa.open_first_view_role(cards[0])
    lever = LeverPage(driver)
    assert lever.is_loaded(), "View Role did not open a Lever application page"

def test_qa_job_fields(driver, qa_url):
    qa = QAJobsPage(driver).open()
    qa.click_see_all_jobs()
    qa.apply_filters()
    cards = qa.get_job_cards()
    for idx, card in enumerate(cards, start=1):
        assert qa.verify_job_card_fields(card), f"Job card #{idx} fields are invalid"
