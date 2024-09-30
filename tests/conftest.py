import pytest
from playwright.async_api import async_playwright

# Fixture to launch browser based on parameter (Chromium, Firefox, WebKit)
@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
async def browser_type(request):
    """Launch the browser based on the parameter."""
    browser = None
    try:
        print(f"Launching {request.param} browser")
        async with async_playwright() as p:
            # Set headless=False to see the browser, or True to run in headless mode
            browser = await getattr(p, request.param).launch(headless=True)
            print(f"{request.param} browser launched successfully.")
            yield browser, request.param  # Yield both browser instance and browser type
    except Exception as e:
        print(f"Error launching {request.param} browser: {e}")
    finally:
        if browser:
            await browser.close()
            print(f"{request.param} browser closed.")

# Fixture to create a new page in the browser for each test
@pytest.fixture(scope="function")
async def page(browser_type):
    """Create and yield a new page for each test."""
    browser, browser_name = browser_type
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await page.close()
    await context.close()

# Fixture to set a global timeout for page actions
@pytest.fixture(scope="function")
async def set_global_timeout(page):
    """Set a default timeout for page actions."""
    try:
        if not page:
            raise ValueError("The page object is not initialized properly.")
        await page.set_default_timeout(60000)  # 60 seconds timeout
    except Exception as e:
        print(f"Error setting global timeout: {e}")
