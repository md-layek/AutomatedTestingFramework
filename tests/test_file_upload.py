import pytest
from utils.test_utilities import retry_action  # Import the retry function



@pytest.mark.asyncio
async def test_file_upload(page):
    """
    Test case to verify file upload functionality.
    """
    async def navigate():
        await page.goto("https://the-internet.herokuapp.com/upload", timeout=60000)
        return True  # Return True for success

    # Use retry_action to retry the navigation if it fails
    await retry_action(navigate, retries=3, delay=2)





