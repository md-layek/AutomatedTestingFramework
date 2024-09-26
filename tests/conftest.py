
import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser_type(request):
    """Parameterized fixture to run tests across multiple browsers."""
    return request.param


@pytest.fixture(scope="session")
def browser(browser_type):
    """Launch browser in headless mode for CI environments."""
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)  # Headless mode for CI
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Create and yield a new page for each test."""
    page = browser.new_page()
    yield page
    page.close()
