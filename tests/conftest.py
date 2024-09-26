import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser_type(request):
    """Parameterized fixture to run tests across multiple browsers."""
    return request.param

@pytest.fixture(scope="session")
def browser(browser_type):
    """Launch browser in headless mode by default, but allow non-headless mode locally."""
    headless = os.getenv("HEADLESS", "true").lower() == "true"  # Headless by default, can be overridden
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=headless)  # Use headless setting
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Create and yield a new page for each test."""
    page = browser.new_page()
    yield page
    page.close()
