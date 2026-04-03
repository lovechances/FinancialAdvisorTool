from app.browser import open_page
from app.scraper import scrape_story_pipeline

TARGET_URL = "https://finance.yahoo.com/"


def main():
    playwright, browser, page = open_page(TARGET_URL)

    try:
        result = scrape_story_pipeline(page)

        print("\n=== MULTI-PAGE SCRAPE RESULT ===")
        print("Source section:", result["source_section"])
        print("Source selector:", result["source_selector"])
        print("Source count:", result["source_count"])
        print()

        for article in result["articles"]:
            print("Headline:", article["headline"])
            print("Href:", article["href"])
            print("Article preview:", article["article_body"])
            print("-" * 80)

    finally:
        browser.close()
        playwright.stop()


if __name__ == "__main__":
    main()