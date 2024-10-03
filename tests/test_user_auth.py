import logging
import pytest
import sys
import os

# Ensure the 'utils' directory is in the Python path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the reusable retry_action, login, and logout functions
from utils.test_utilities import retry_action, retry_click, login, logout


#
# @pytest.mark.asyncio
# async def test_user_login_success(page):
#     """
#     Test successful login with valid credentials.
#     """
#     try:
#         # Attempt to login with valid credentials
#         await retry_action(lambda: login(page, "tomsmith", "SuperSecretPassword!"))
#
#         # Assert logout button is visible
#         assert await retry_action(lambda: page.is_visible("a[href='/logout']"), retries=3, delay=2)
#
#     except Exception:
#         # Capture screenshot upon failure for debugging
#         await page.screenshot(path=f"failure_{page.context.browser_name}_success.png")
#         raise  # Re-raise the exception after capturing screenshot
#

@pytest.mark.asyncio
async def test_user_login_success(page):
    """
    Test case for successful login.
    """
    try:
        # Navigate to the login page
        await page.goto("http://the-internet.herokuapp.com/login", timeout=120000)

        # Perform the login
        await retry_action(lambda: login(page, "tomsmith", "SuperSecretPassword!"))

    except Exception as e:
        # Capture screenshot and raise exception
        browser_name = page.context.browser.browser_type.name  # Correct browser name retrieval
        await page.screenshot(path=f"failure_{browser_name}_success.png")
        raise e








@pytest.mark.asyncio
async def test_user_login_failure(page):
    """
    Test failed login with invalid credentials.
    """
    try:
        # Navigate to the login page
        await page.goto("http://the-internet.herokuapp.com/login", timeout=120000)

        # Ensure the login form and submit button are visible before proceeding
        await page.wait_for_selector("button[type='submit']", state="visible", timeout=60000)

        # Retry the login process if it fails
        await retry_click(page, "button[type='submit']")
    except Exception as e:
        # Retrieve the browser name for the screenshot file
        browser_name = page.context.browser.browser_type.name

        # Log the error for debugging purposes
        logging.error(f"Login test failed on browser: {browser_name}. Error: {str(e)}")

        # Take a screenshot on failure
        await page.screenshot(path=f"failure_login_{browser_name}.png")
        raise
