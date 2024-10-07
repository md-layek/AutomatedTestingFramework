import pytest

@pytest.mark.asyncio
async def test_cross_browser(page):
    """
    Test case to verify cross-browser compatibility.
    """
    # Navigate to the test page with a longer timeout
    await page.goto("https://the-internet.herokuapp.com/", timeout=120000)

    # Wait for the page to load completely
    await page.wait_for_load_state("load")

    # Verify the title or any other element
    title = await page.title()
    assert "The Internet" in title, f"Expected 'The Internet' in title, but got {title}"