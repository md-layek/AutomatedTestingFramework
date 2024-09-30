import pytest
import asyncio
from playwright.async_api import Page


# Test to verify dropdown selection
@pytest.mark.asyncio
async def test_select_dropdown(page: Page):
    """
    Test case to verify dropdown selection.
    """
    # Navigate to the dropdown page
    await page.goto("http://the-internet.herokuapp.com/dropdown", timeout=60000)

    # Select an option and verify it was selected
    await page.select_option("#dropdown", "1")
    selected_value = await page.input_value("#dropdown")
    assert selected_value == "1", f"Expected '1' to be selected, but got '{selected_value}'"


# Retry logic for click actions with additional debug information
async def retry_click(page: Page, selector: str, retries=3, delay=2):
    for attempt in range(retries):
        try:
            print(f"Attempting click {attempt + 1}/{retries} for element: {selector}")
            await page.click(selector, timeout=60000, force=True)
            return  # Exit if the click is successful
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)  # Wait before retrying
            else:
                raise  # Re-raise the exception if max retries reached


@pytest.mark.asyncio
async def test_user_login_failure(page: Page):
    """
    Test failed login with invalid credentials.
    """
    # Navigate to the login page
    await page.goto("http://the-internet.herokuapp.com/login", timeout=60000)

    # Ensure the login form and submit button are visible
    await page.wait_for_selector("button[type='submit']", state="visible", timeout=60000)

    # Input invalid credentials
    await page.fill("input[name='username']", "invalidUser")
    await page.fill("input[name='password']", "invalidPassword")

    # Retry clicking the submit button
    await retry_click(page, "button[type='submit']")

    # Verify the error message is displayed
    error_message = await page.text_content("#flash")
    assert "Your username is invalid!" in error_message, f"Unexpected error message: {error_message}"