import pytest

@pytest.mark.asyncio
async def test_select_dropdown(page, set_global_timeout):
    """
    Test case to verify dropdown selection.
    """
    # Navigate to the dropdown page
    await page.goto("http://the-internet.herokuapp.com/dropdown")

    # Select an option and verify it was selected
    await page.select_option("#dropdown", "1")
    selected_value = await page.input_value("#dropdown")
    assert selected_value == "1", f"Expected '1' to be selected, but got '{selected_value}'"


@pytest.mark.asyncio
async def test_js_alerts(page, set_global_timeout):
    """
    Test case to verify handling of JavaScript alerts.
    """
    # Navigate to the JavaScript alerts page
    await page.goto("http://the-internet.herokuapp.com/javascript_alerts")

    # Trigger a JavaScript alert and accept it
    async with page.expect_event("dialog") as dialog_info:
        await page.click("button[onclick='jsAlert()']")
    alert = await dialog_info.value
    await alert.accept()

    # Verify the result message on the page after the alert is accepted
    result_text = await page.text_content("#result")
    assert "You successfully clicked an alert" in result_text, f"Unexpected result text: {result_text}"
