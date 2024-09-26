def test_ci_integration(page):
    """
    Test case to verify basic functionality works in a CI environment.
    """

    # Navigate to the Herokuapp page for testing
    page.goto("https://the-internet.herokuapp.com/")

    # Assert that the page title is correct
    assert page.title() == "The Internet"

    # Wait for the "Form Authentication" link to be visible and interactable before clicking
    page.wait_for_selector("a[href='/login']", timeout=10000)  # Wait for up to 10 seconds for the element to appear
    page.click("a[href='/login']")

    # Assert that the login page loads correctly
    assert "Login Page" in page.text_content("h2")

    # Attempt a login using valid credentials
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    # Assert that the login was successful
    assert "You logged into a secure area!" in page.text_content("div.flash.success")

    # Finally, logout to end the session
    page.click("a[href='/logout']")

    # Assert that the logout was successful
    assert "You logged out of the secure area!" in page.text_content("div.flash.success")
