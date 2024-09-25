import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser_type(request):
    """Parametrized fixture for running tests on multiple browsers."""
    return request.param

@pytest.fixture(scope="session")
def browser(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


