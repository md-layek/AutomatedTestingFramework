# Functional Tests

import pytest
@pytest.mark.asyncio
@pytest.mark.flaky(reruns=2, reruns_delay=5)
async def test_dynamic_content(page):
    """
    Test to handle dynamic content.
    """
    # Navigate to the dynamic content page (increase timeout)
    print("Navigating to the dynamic content page.")
    await page.goto("http://the-internet.herokuapp.com/dynamic_content", timeout=180000)
    print("Successfully navigated to the dynamic content page.")

    # Verify the presence of dynamic content
    print("Verifying the presence of dynamic content.")
    content = await page.content()
    assert "Dynamic Content" in content, "Dynamic content not found"
    print("Dynamic content verified successfully.")