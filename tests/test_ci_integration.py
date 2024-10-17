# Integration Tests
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utilities import retry_action  # Import the retry function


@pytest.mark.asyncio
async def test_ci_integration(page):
    """
    Test case to verify basic functionality works in a CI environment.
    """

    # Check if running in CI environment, log a warning if not in CI
    if "CI" not in os.environ:
        print("Warning: CI environment variable is not set. Running test outside of CI.")

    # Log the browser being used
    browser_name = page.context.browser.browser_type.name
    print(f"Running test on browser: {browser_name}")

    async def load_page():
        await page.goto("https://the-internet.herokuapp.com/", timeout=60000)
        return True  # Ensure this returns True for success

    # Use retry mechanism in case of temporary issues
    await retry_action(load_page)

    # Verify page content after loading (e.g., check if a specific element exists)
    assert await page.query_selector("h1") is not None, "Header element not found on the page"

    # Additional assertion to ensure successful page load
    title = await page.title()
    assert title == "The Internet", f"Unexpected page title: {title}"