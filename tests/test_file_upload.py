def test_file_upload(page):
    """
    Test case to verify file upload functionality.
    """
    # Navigate to the file upload page
    page.goto("https://the-internet.herokuapp.com/upload")

    # Upload a file (ensure the file exists in the specified path)
    file_path = "tests/files/testfile.txt"  # Replace with the actual path to your file
    page.set_input_files("#file-upload", file_path)

    # Click the submit button to upload the file
    page.click("#file-submit")

    # Assert that the file was uploaded successfully by checking the confirmation message
    assert "File Uploaded!" in page.text_content("h3")
