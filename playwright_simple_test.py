import asyncio
from playwright.async_api import async_playwright

async def run_playwright_test():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            print(f"Launching {browser_type.name} browser")
            browser = await browser_type.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("https://the-internet.herokuapp.com/")
            print(f"Page title: {await page.title()}")
            await page.close()
            await context.close()
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_playwright_test())
