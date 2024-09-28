import pytest

@pytest.mark.asyncio
async def test_dynamic_content(page):
    """
    Test case to verify dynamic content is loaded correctly.
    """
    # Navigate to the Dynamic Content page
    await page.goto("http://the-internet.herokuapp.com/dynamic_content")

    # Check that dynamic content (e.g., images) is loaded
    assert await page.is_visible("div#content div:nth-child(1) img"), "Image 1 not visible"
    assert await page.is_visible("div#content div:nth-child(2) img"), "Image 2 not visible"
