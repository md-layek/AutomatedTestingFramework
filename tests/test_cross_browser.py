def test_cross_browser(playwright, browser_type):
    """
    Test case to verify cross-browser compatibility using Playwright's browser_type.
    This will automatically run on Chromium, Firefox, and WebKit based on pytest-playwright config.
    """
    # Launch the browser based on browser_type passed by Playwright
    browser = playwright[browser_type].launch(headless=True)

    # Create a new browser context and page
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the login page
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill out the login form
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    # Assert login was successful
    assert "You logged into a secure area!" in page.text_content("#flash")

    # Close the context and browser
    context.close()
    browser.close()
