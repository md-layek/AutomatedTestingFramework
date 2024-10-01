import pytest
import sys
import os

# Ensure the 'utils' directory is in the Python path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the reusable retry_action, login, and logout functions
from utils.test_utilities import retry_action, retry_click, login, logout



@pytest.mark.asyncio
async def test_user_login_success(page):
    """
    Test successful login with valid credentials.
    """
    await retry_action(lambda: login(page, "tomsmith", "SuperSecretPassword!"))

    # Assert logout button is visible
    assert await retry_action(lambda: page.is_visible("a[href='/logout']"), retries=3, delay=2)

@pytest.mark.asyncio
async def test_user_login_failure(page):
    """
    Test failed login with invalid credentials using retry logic.
    """
    await retry_action(lambda: login(page, "invalidUser", "invalidPassword"))

    # Verify error message after the failed login attempt
    error_message = await page.text_content("#flash")
    assert "Your username is invalid!" in error_message
