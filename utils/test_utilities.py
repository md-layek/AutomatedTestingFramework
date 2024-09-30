import asyncio
async def login(page, username, password):
    """
    Reusable function to log in a user asynchronously.
    """
    # Navigate to the login page
    await page.goto("http://the-internet.herokuapp.com/login")

    # Fill in the username and password fields
    await page.fill("#username", username)
    await page.fill("#password", password)

    # Submit the login form
    await page.click("button[type='submit']")


async def logout(page):
    """
    Reusable function to log out a user asynchronously.
    """
    # Click the logout button and verify successful logout
    await page.click("a[href='/logout']")


async def retry_action(action, retries=3, delay=2):
    """
    Retries an async action a specified number of times.

    :param action: The async function to execute.
    :param retries: Number of retries before failing.
    :param delay: Delay (in seconds) between retries.
    """
    for attempt in range(retries):
        try:
            await action()  # Execute the async action
            return  # If it succeeds, exit the loop
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)  # Wait before retrying
            else:
                raise  # Re-raise the exception if all retries fail


