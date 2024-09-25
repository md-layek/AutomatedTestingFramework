def login(page, username, password):
    """Reusable function to log in a user."""
    page.goto("http://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")


def logout(page):
    """Reusable function to log out a user."""
    # Click the logout button and verify successful logout
    page.click("a[href='/logout']")
