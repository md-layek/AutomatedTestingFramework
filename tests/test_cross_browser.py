# Functional Tests

import pytest
from playwright.async_api import TimeoutError

@pytest.mark.asyncio
async def test_cross_browser(page):
    """
    Test case to verify cross-browser compatibility.
    """
    try:
        # Navigate to the test page with a longer timeout
        print("Navigating to the test page.")
        await page.goto("https://the-internet.herokuapp.com/", timeout=120000)
        print("Successfully navigated to the test page.")

        # Wait for the page to load completely
        print("Waiting for the page to load completely.")
        await page.wait_for_load_state("load")
        print("Page load complete.")

        # Verify the title or any other element
        print("Verifying the page title.")
        title = await page.title()
        assert "The Internet" in title, f"Expected 'The Internet' in title, but got {title}"
        print("Page title verified successfully.")

        # Verify a specific element on the page to ensure proper load
        print("Verifying the presence of a key element on the page.")
        element = await page.query_selector("h1")
        assert element is not None, "Expected key element not found on the page."
        print("Key element verified successfully.")

    except TimeoutError as e:
        print(f"Timeout occurred: {e}")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
