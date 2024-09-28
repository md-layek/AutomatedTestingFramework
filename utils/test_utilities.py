async def login(page, username, password):
    """
    Reusable function to log in a user asynchronously.
    """
    # Navigate to the login page
    await page.goto("http://the-internet.herokuapp.com/login")

    # Fill in the username and password fields
    await page.fill("#username", username)
    await page.fill("#password", password)

    # Submit the login form
    await page.click("button[type='submit']")


async def logout(page):
    """
    Reusable function to log out a user asynchronously.
    """
    # Click the logout button and verify successful logout
    await page.click("a[href='/logout']")
