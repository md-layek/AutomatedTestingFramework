import pytest
@pytest.mark.asyncio
async def test_cross_browser(page):
    """Test case to run across Chromium, Firefox, and WebKit."""
    # Navigate to the test page
    await page.goto("https://the-internet.herokuapp.com/")

    # Verify the page title
    assert await page.title() == "The Internet"
