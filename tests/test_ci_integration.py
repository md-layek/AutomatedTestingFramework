import pytest

@pytest.mark.asyncio
async def test_ci_integration(page):
    """
    Test case to verify basic functionality works in a CI environment.
    """
    # Navigate to the test page
    await page.goto("https://the-internet.herokuapp.com/")

    # Assert the title is correct
    title = await page.title()
    assert title == "The Internet", f"Expected title to be 'The Internet' but got '{title}'"

    # Additional actions and assertions can be added as needed
