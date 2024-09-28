import pytest

@pytest.mark.asyncio
async def test_file_upload(page):
    """
    Test case to verify file upload functionality.
    """
    # Navigate to the file upload page
    await page.goto("https://the-internet.herokuapp.com/upload")

    # Ensure the file input element is visible
    upload_input = page.locator("#file-upload")
    await upload_input.wait_for(state="visible", timeout=60000)  # Increased timeout to 60 seconds

    # Upload a file
    file_path = "tests/files/testfile.txt"  # Ensure correct file path
    await page.set_input_files("#file-upload", file_path)

    # Click the submit button after uploading
    await page.click("#file-submit")

    # Verify file upload success
    success_message = await page.text_content("h3")
    assert "File Uploaded!" in success_message
