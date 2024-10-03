import pytest
from playwright.async_api import Page

alert_message = None  # Define a global variable for the alert message


# Test to verify dropdown selection
@pytest.mark.asyncio
async def test_select_dropdown(page: Page):
    """
    Test case to verify dropdown selection.
    """
    # Navigate to the dropdown page
    await page.goto("http://the-internet.herokuapp.com/dropdown", timeout=120000)

    # Select an option and verify it was selected
    await page.select_option("#dropdown", "1")
    selected_value = await page.input_value("#dropdown")
    assert selected_value == "1", f"Expected '1' to be selected, but got '{selected_value}'"


# Test to handle JavaScript alerts
@pytest.mark.asyncio
async def test_javascript_alerts(page: Page):
    """
    Test case to handle JavaScript alerts.
    """
    global alert_message  # Refer to the global variable

    # Event listener for JavaScript alert dialogs
    page.on("dialog", handle_dialog)

    try:
        # Navigate to the JavaScript Alerts page
        await page.goto("http://the-internet.herokuapp.com/javascript_alerts", timeout=120000)

        # Trigger the JS Alert
        await page.click("button[onclick='jsAlert()']")

        # Verify that the correct alert message was displayed
        assert alert_message == "I am a JS Alert", f"Expected 'I am a JS Alert', but got '{alert_message}'"

    except Exception as e:
        # Take a screenshot on failure
        browser_name = page.context.browser.browser_type.name
        await page.screenshot(path=f"failure_javascript_alert_{browser_name}.png")
        raise e


async def handle_dialog(dialog):
    """
    Asynchronously handle the dialog event and store the message.
    """
    global alert_message
    alert_message = dialog.message
    await dialog.accept()
