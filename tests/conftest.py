import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
async def browser_type(request):
    """Launch the browser based on the parameter."""
    try:
        print(f"Launching {request.param} browser")
        async with async_playwright() as p:
            browser = await getattr(p, request.param).launch(headless=True)
            print(f"{request.param} browser launched successfully.")
            yield browser
    except Exception as e:
        print(f"Error launching {request.param} browser: {e}")
    finally:
        if 'browser' in locals() and browser:
            await browser.close()
            print(f"{request.param} browser closed.")

@pytest.fixture(scope="function")
async def page(browser_type):
    """Create and yield a new page for each test."""
    context = None
    page = None
    try:
        print("Creating new browser context.")
        context = await browser_type.new_context()
        print("Context created. Opening new page.")
        page = await context.new_page()
        print("New page opened.")
        yield page
    except Exception as e:
        print(f"Error creating page: {e}")
    finally:
        if page:
            print("Closing page.")
            await page.close()
        if context:
            print("Closing context.")
            await context.close()

@pytest.fixture(scope="function")
async def set_global_timeout(page):
    """Set a default timeout for page actions."""
    try:
        if not page:
            raise ValueError("The page object is not initialized properly.")
        await page.set_default_timeout(60000)  # 60 seconds timeout
    except Exception as e:
        print(f"Error setting global timeout: {e}")
