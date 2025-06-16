import asyncio
from playwright.async_api import async_playwright

async def scrape_chapter(
    url: str,
    screenshot_path: str = 'chapter_screenshot.png',
    save_text_path: str = 'chapter_text.txt'
):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"🌐 Navigating to {url}")
        await page.goto(url)

        # Wait until the content is loaded
        await page.wait_for_selector('#mw-content-text')

        # Take a full-page screenshot
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"✅ Screenshot saved at: {screenshot_path}")

        # Extract the main text content
        content = await page.inner_text('#mw-content-text')
        with open(save_text_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Chapter text saved at: {save_text_path}")

        await browser.close()

# Run the script
if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    asyncio.run(scrape_chapter(url))
