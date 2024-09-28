import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
async def browser_type(request):
    """Launch the browser based on the parameter."""
    async with async_playwright() as p:
        browser = await getattr(p, request.param).launch(headless=True)
        yield browser
        await browser.close()

#@pytest.fixture(scope="function")
#async def page(browser_type):
    """Create and yield a new page for each test."""
 #   context = await browser_type.new_context()
  #  page = await context.new_page()
   # yield page
    #await page.close()
    #await context.close()



@pytest.fixture(scope="function")
async def page(browser_type):
    """Create and yield a new page for each test."""
    try:
        context = await browser_type.new_context()
        page = await context.new_page()
        print("Page successfully created.")
        yield page
    except Exception as e:
        print(f"Error during page creation: {e}")
    finally:
        await page.close()
        await context.close()



@pytest.fixture(scope="function")
async def set_global_timeout(page):
    """Set a default timeout for page actions."""
    if not page:
        raise ValueError("The page object is not initialized properly.")
    await page.set_default_timeout(60000)  # 60 seconds timeout
