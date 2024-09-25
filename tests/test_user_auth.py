import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.test_utilities import login, logout

def test_user_login_success(page):
    """
    Test case to verify successful login using valid credentials.
    """
    # Use the reusable login function
    login(page, "tomsmith", "SuperSecretPassword!")

    # Assert that the login was successful
    assert "You logged into a secure area!" in page.text_content("div.flash.success")

    # Use the reusable logout function
    logout(page)

    # Assert that the logout was successful
    assert "You logged out of the secure area!" in page.text_content("div.flash.success")


def test_user_login_failure(page):
    """
    Test case to verify failed login using invalid credentials.
    """
    # Use the reusable login function with invalid credentials
    login(page, "invalidUser", "invalidPassword")

    # Assert that the login failed
    assert "Your username is invalid!" in page.text_content("div.flash.error")
