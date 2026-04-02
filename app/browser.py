from playwright.sync_api import sync_playwright


def open_page(url: str):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    return playwright, browser, page