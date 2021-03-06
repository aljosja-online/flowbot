import asyncio
import pyppeteer


async def main():
    browser = await pyppeteer.launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://nu.nl/')
    await page.screenshot(path='nu.png', fullPage=True)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
