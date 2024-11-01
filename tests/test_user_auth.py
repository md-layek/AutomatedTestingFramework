# # Functional Tests
import os
import logging
import pytest
import sys

# Ensure the 'utils' directory is in the Python path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the reusable retry_action, retry_click, login, and logout functions
from utils.test_utilities import retry_action, retry_click, login, logout

logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')

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

        # Perform logout after login
        await retry_action(lambda: logout(page))

    except Exception as e:
        # Capture screenshot and raise exception
        browser_name = page.context.browser.browser_type.name  # Correct browser name retrieval
        screenshot_path = os.path.join(logs_dir, f"failure_{browser_name}_success.png")
        await page.screenshot(path=screenshot_path)
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
        screenshot_path = os.path.join(logs_dir, f"failure_login_{browser_name}.png")
        await page.screenshot(path=screenshot_path)
        raise