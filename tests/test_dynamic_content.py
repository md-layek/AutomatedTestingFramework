import pytest

@pytest.mark.asyncio
async def test_dynamic_content(page):
    """
    Test case to verify dynamic content is loaded correctly.
    """
    # Navigate to the Dynamic Content page with increased timeout
    await page.goto("http://the-internet.herokuapp.com/dynamic_content", timeout=60000)

    # Wait for the dynamic content to load
    await page.wait_for_selector(".large-10.columns", state="visible", timeout=60000)

    # Verify the dynamic content has loaded
    content = await page.text_content(".large-10.columns")
    assert content is not None, "Dynamic content did not load as expected."
