import pytest

@pytest.mark.asyncio
async def test_select_dropdown(page):
   """
   Test case to verify dropdown selection.
   """
   # Navigate to the dropdown page
   await page.goto("http://the-internet.herokuapp.com/dropdown", timeout=60000)


   # Select an option and verify it was selected
   await page.select_option("#dropdown", "1")
   selected_value = await page.input_value("#dropdown")
   assert selected_value == "1", f"Expected '1' to be selected, but got '{selected_value}'"





import asyncio  # Add this for sleep

@pytest.mark.asyncio
async def test_js_alerts(page):
    # Navigate to the JavaScript alerts page
    await page.goto("http://the-internet.herokuapp.com/javascript_alerts", timeout=60000)

    # Ensure the element is visible and ready
    await page.wait_for_selector("button[onclick='jsAlert()']", state="visible", timeout=60000)

    # Additional debug information
    is_visible = await page.is_visible("button[onclick='jsAlert()']")
    is_enabled = await page.is_enabled("button[onclick='jsAlert()']")
    print(f"Element visible: {is_visible}, enabled: {is_enabled}")

    # Add an explicit wait before the click
    await asyncio.sleep(1)  # Give some time for the element to be fully interactable

    # Trigger a JavaScript alert and accept it
    async with page.expect_event("dialog") as dialog_info:
        #await page.click("button[onclick='jsAlert()']", timeout=60000)
        await page.click("button[onclick='jsAlert()']", timeout=60000, force=True)

    alert = await dialog_info.value
    await alert.accept()

    # Verify the result message on the page after the alert is accepted
    result_text = await page.text_content("#result")
    assert "You successfully clicked an alert" in result_text, f"Unexpected result text: {result_text}"
