from app.browser import open_page
from app.scraper import scrape_visible_text


TARGET_URL = "https://finance.yahoo.com/"


def main():
    playwright, browser, page = open_page(TARGET_URL)

    try:
        result = scrape_visible_text(page)

        print("\n=== SCRAPE RESULT ===")
        print("Title:", result["title"])
        print("Word count:", result["word_count"])
        print("\nPreview:\n")
        print(result["preview"])

    finally:
        browser.close()
        playwright.stop()


if __name__ == "__main__":
    main()