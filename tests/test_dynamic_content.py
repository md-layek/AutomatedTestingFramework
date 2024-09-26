def test_dynamic_content(page):
    """
    Test case to verify dynamic content is loaded correctly.
    """
    # Navigate to the Dynamic Content page
    page.goto("http://the-internet.herokuapp.com/dynamic_content")

    # Check that dynamic content (e.g., images) is loaded
    assert page.is_visible("div#content div:nth-child(1) img")
    assert page.is_visible("div#content div:nth-child(2) img")
