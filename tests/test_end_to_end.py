#E2E Tests
import pytest
import os
import sys
from playwright.async_api import TimeoutError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utilities import login, logout, retry_action

@pytest.mark.asyncio
async def test_end_to_end_workflow(page):
    """
    End-to-end test simulating a complete user journey.
    """
    try:
        # Step 1: Perform login using the utility function
        print("Logging in with utility function.")
        await retry_action(lambda: login(page, username="tomsmith", password="SuperSecretPassword!"))
        print("Login successful.")

        # Step 2: Navigate to dynamic content page and verify content
        print("Navigating to dynamic content page.")
        await page.goto("https://the-internet.herokuapp.com/dynamic_content", timeout=60000)
        print("Dynamic content page loaded. Verifying content.")
        assert "Dynamic Content" in await page.content(), "Dynamic content not found"
        print("Dynamic content verified successfully.")

        # Step 3: Navigate to file upload page and upload a file
        print("Navigating to file upload page.")
        await page.goto("https://the-internet.herokuapp.com/upload", timeout=60000)
        print("Uploading a file.")
        await page.set_input_files("input#file-upload", "tests/files/testfile.txt")
        await page.click("input#file-submit", timeout=30000)

        # Explicitly wait for the file upload result element
        print("Waiting for the file upload result.")
        assert await page.is_visible("div#uploaded-files"), "File upload failed"
        print("File uploaded successfully.")

        # Step 4: Logout using the utility function
        print("Logging out with utility function.")
        await retry_action(lambda: logout(page))
        print("Logout successful.")

    except TimeoutError as e:
        print(f"Timeout occurred: {e}")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
