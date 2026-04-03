from app.browser import open_page
from app.scraper import scrape_story_cards

TARGET_URL = "https://finance.yahoo.com/"


def main():
    playwright, browser, page = open_page(TARGET_URL)

    try:
        result = scrape_story_cards(page)

        print("\n=== SCRAPE RESULT ===")
        print("Section name:", result["section_name"])
        print("Selector used:", result["selector_used"])
        print("Selector counts:", result["selector_counts"])
        print("Item count:", result["item_count"])
        print()

        for item in result["items"]:
            print("Index:", item["index"])
            print("Headline:", item["headline"])
            print("Href:", item["href"])
            print("-" * 60)

    finally:
        browser.close()
        playwright.stop()


if __name__ == "__main__":
    main()