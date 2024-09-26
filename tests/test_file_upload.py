def test_form_submission(page):
    """
    Test case to verify form submission with valid data.
    """
    # Navigate to the form submission page
    page.goto("https://the-internet.herokuapp.com/contact_form")  # Example form page URL

    # Fill out the form fields
    page.fill("#name", "John Doe")  # Assuming the form has an input field for name
    page.fill("#email", "johndoe@example.com")  # Assuming the form has an input field for email
    page.fill("#message", "This is a test message.")  # Assuming the form has a textarea for the message

    # Submit the form
    page.click("#submit-button")  # Assuming there is a submit button with this selector

    # Assert success message after form submission
    assert "Thank you for your message" in page.text_content("#success-message")  # Assuming success message is shown here
