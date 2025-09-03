import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    return "https://useinsider.com/"


@pytest.fixture(scope="session")
def qa_url():
    return "https://useinsider.com/careers/quality-assurance/"


@pytest.fixture(scope="session")
def screenshots_dir():
    path = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(path, exist_ok=True)
    return path


@pytest.fixture
def driver():
    """Initialize Chrome WebDriver (headless by default)."""
    headless_env = os.getenv("HEADLESS", "true").lower()
    headless = headless_env not in ("false", "0", "no")

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # -----------------------------
    # Google servislerini kapatmak için eklenen seçenekler
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-logging")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-component-update")
    options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees,OptimizationHints")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-ipc-flooding-protection")
    # -----------------------------

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()


# Screenshot alma hook'u (sadece bu kalsın!)
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot if any test step fails."""
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        driver = item.funcargs.get("driver", None)
        screenshots_dir = item.funcargs.get("screenshots_dir", None)
        if driver is not None and screenshots_dir is not None:
            ts = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{item.name}_{rep.when}_{ts}.png"
            path = os.path.join(screenshots_dir, filename)
            try:
                driver.save_screenshot(path)
                print(f"\n[pytest] Saved screenshot: {path}")
            except Exception as e:
                print(f"\n[pytest] Could not save screenshot: {e}")
