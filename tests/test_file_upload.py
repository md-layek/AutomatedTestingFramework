import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utilities import retry_action  # Import the retry function

@pytest.mark.asyncio
async def test_file_upload(page):
    """
    Test case to verify file upload functionality.
    """
    # Define the path to the file you want to upload
    file_to_upload = os.path.abspath("tests/files/testfile.txt")  # Update with the actual file path

    async def navigate():
        # Navigate to the file upload page
        await page.goto("https://the-internet.herokuapp.com/upload", timeout=60000)
        return True  # Return True for success

    # Use retry_action to retry the navigation if it fails
    await retry_action(navigate, retries=3, delay=2)

    # Locate the file input element and upload the file
    await page.set_input_files("input[type='file']", file_to_upload)

    # Submit the file upload form
    await page.click("input[type='submit']")

    # Verify that the file was uploaded successfully
    success_message = await page.inner_text("#uploaded-files")
    assert success_message == "testfile.txt", f"Expected 'file.txt', but got '{success_message}'"




