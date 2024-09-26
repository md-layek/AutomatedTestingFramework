def test_select_dropdown(page):
    """
    Test case to verify dropdown selection.
    """
    # Navigate to the Dropdown page
    page.goto("http://the-internet.herokuapp.com/dropdown")

    # Select an option from the dropdown
    page.select_option("select#dropdown", "2")

    # Assert that the correct option was selected
    selected_option = page.query_selector("select#dropdown option[selected]")
    assert selected_option.text_content() == "Option 2"


def test_js_alerts(page):
    """
    Test case to verify handling of JavaScript alerts.
    """
    # Navigate to the JavaScript Alerts page
    page.goto("http://the-internet.herokuapp.com/javascript_alerts")

    # Click the button to trigger a JS alert
    page.click("button[onclick='jsAlert()']")

    # Accept the alert
    page.on("dialog", lambda dialog: dialog.accept())

    # Assert that the alert was accepted successfully
    assert "You successfully clicked an alert" in page.text_content("#result")
