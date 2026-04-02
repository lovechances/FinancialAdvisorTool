from app.browser import open_page
from app.scraper import scrape_story_cards

TARGET_URL = "https://finance.yahoo.com/"


def main():
    playwright, browser, page = open_page(TARGET_URL)

    try:
        result = scrape_story_cards(page)

        print("\n=== SCRAPE RESULT ===")
        print("Count:", result["item_count"])

        for item in result["items"]:
            print("Headline:", item["headline"])
            print("Href:", item["href"])
            print("-" * 50)

    finally:
        browser.close()
        playwright.stop()


if __name__ == "__main__":
    main()