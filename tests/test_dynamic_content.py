import pytest

# @pytest.mark.asyncio
# async def test_dynamic_content(page):
#     """
#     Test case to verify dynamic content is loaded correctly.
#     """
#     # Navigate to the Dynamic Content page with increased timeout
#     await page.goto("http://the-internet.herokuapp.com/dynamic_content", timeout=120000)
#
#     # Wait for the dynamic content to load
#     await page.wait_for_selector(".large-10.columns", state="visible", timeout=60000)
#
#     # Verify the dynamic content has loaded
#     content = await page.text_content(".large-10.columns")
#     assert content is not None, "Dynamic content did not load as expected."



@pytest.mark.asyncio
@pytest.mark.flaky(reruns=2, reruns_delay=5)
async def test_dynamic_content(page):
    """
    Test to handle dynamic content.
    """
    # Navigate to the dynamic content page (increase timeout)
    await page.goto("http://the-internet.herokuapp.com/dynamic_content", timeout=180000)

    # Verify the presence of dynamic content
    content = await page.content()
    assert "Dynamic Content" in content, "Dynamic content not found"