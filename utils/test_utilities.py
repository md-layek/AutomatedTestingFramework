import asyncio
async def login(page, username, password):
    """
    Reusable function to log in a user asynchronously.
    """
    await page.goto("http://the-internet.herokuapp.com/login")
    await page.fill("#username", username)
    await page.fill("#password", password)
    await page.click("button[type='submit']")
    return True  # Return True to indicate success


async def logout(page):
    await page.click("a[href='/logout']")
    return True  # Return True to indicate success

async def retry_action(action, retries=3, delay=2):
    """
    Retries an async action a specified number of times.
    :param action: The async function to execute.
    :param retries: Number of retries before failing.
    :param delay: Delay (in seconds) between retries.
    :return: The result of the action, or raises an exception after max retries.
    """
    for attempt in range(retries):
        try:
            result = await action()  # Execute the async action and store the result
            return True  # If no exception, return True indicating success
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)  # Wait before retrying
            else:
                raise  # Re-raise the exception after max retries




async def retry_click(page, selector, retries=3, delay=2):
    """
    Retries clicking a selector up to 'retries' number of times, with 'delay' seconds between attempts.
    """
    for attempt in range(retries):
        try:
            # Wait for the selector to be visible
            await page.wait_for_selector(selector, state="visible", timeout=60000)
            # Ensure the element is enabled before clicking
            if await page.is_enabled(selector):
                await page.click(selector)
                return  # Success, exit the function
            else:
                print(f"Attempt {attempt + 1} failed: Selector is not enabled")
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            await asyncio.sleep(delay)
    raise Exception(f"Failed to click {selector} after {retries} retries")

