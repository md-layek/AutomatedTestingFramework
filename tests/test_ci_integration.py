import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utilities import retry_action  # Import the retry function


@pytest.mark.asyncio
async def test_ci_integration(page):
    """
    Test case to verify basic functionality works in a CI environment.
    """

    async def load_page():
        await page.goto("https://the-internet.herokuapp.com/", timeout=60000)
        return True  # Ensure this returns True for success

    # Use retry mechanism in case of temporary issues
    await retry_action(load_page)
