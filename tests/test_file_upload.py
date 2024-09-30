import pytest
from utils.test_utilities import retry_action  # Import the retry function


@pytest.mark.asyncio
async def test_file_upload(page):
    """
    Test case to verify file upload functionality.
    """

    # Define the action to retry: navigating to the file upload page
    async def navigate():
        await page.goto("https://the-internet.herokuapp.com/upload", timeout=60000)

    # Use retry_action to retry the navigation if it fails
    await retry_action(navigate, retries=3, delay=2)

    # Ensure the file input element is visible
    upload_input = page.locator("#file-upload")
    await upload_input.wait_for(state="visible", timeout=60000)

    # Upload a file
    file_path = "tests/files/testfile.txt"  # Ensure correct file path
    await page.set_input_files("#file-upload", file_path)

    # Define the action to retry: clicking the submit button
    async def submit():
        await page.click("#file-submit", timeout=60000)

    # Retry the click action if it fails
    await retry_action(submit, retries=3, delay=2)





