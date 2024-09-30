import pytest
import sys
import os

# Ensure the 'utils' directory is in the Python path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Import the reusable login and logout functions

from utils.test_utilities import login, logout


@pytest.mark.asyncio
async def test_user_login_success(page):
    """
    Test successful login with valid credentials.
    """
    # Navigate to the login page
    await page.goto("http://the-internet.herokuapp.com/login")

    # Perform login with valid credentials
    await login(page, username="tomsmith", password="SuperSecretPassword!")

    # Verify login success message
    assert "You logged into a secure area!" in await page.text_content("div.flash.success")


@pytest.mark.asyncio
async def test_user_login_failure(page):
    """
    Test failed login with invalid credentials.
    """
    # Navigate to the login page
    await page.goto("http://the-internet.herokuapp.com/login")

    # Perform login with invalid credentials
    await login(page, username="invalidUser", password="invalidPassword")

    # Verify login failure message
    assert "Your username is invalid!" in await page.text_content("div.flash.error")



















