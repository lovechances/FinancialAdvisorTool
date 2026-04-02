def scrape_story_cards(page) -> dict:
    page.wait_for_timeout(3000)

    cards = page.locator('[data-testid="storyitem"]')
    count = cards.count()

    items = []

    for i in range(min(count, 12)):
        card = cards.nth(i)
        link = card.locator("a").first

        headline = link.get_attribute("aria-label")
        href = link.get_attribute("href")

        items.append({
            "index": i,
            "headline": headline,
            "href": href,
        })

    return {
        "section_name": "hero_headline_story_items",
        "item_count": len(items),
        "items": items,
    }