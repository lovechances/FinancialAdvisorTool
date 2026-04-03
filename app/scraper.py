def inspect_selector_counts(page) -> dict:
    candidates = {
        "storyitem": '[data-testid="storyitem"]',
        "story_item_li": "li.story-item",
        "article_role": 'section[role="article"]',
        "headline_links": 'a[aria-label]',
    }

    counts = {}

    for name, selector in candidates.items():
        counts[name] = page.locator(selector).count()

    return counts

def choose_story_selector(counts: dict) -> tuple[str, str]:
    if counts["storyitem"] > 0:
        return "storyitem", '[data-testid="storyitem"]'

    if counts["story_item_li"] > 0:
        return "story_item_li", "li.story-item"

    raise RuntimeError("No usable story card selector found.")

def scrape_story_cards(page) -> dict:
    page.wait_for_timeout(3000)

    counts = inspect_selector_counts(page)
    selector_name, card_selector = choose_story_selector(counts)

    cards = page.locator(card_selector)
    count = cards.count()

    items = []

    for i in range(min(count, 10)):
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
        "section_name": selector_name,
        "selector_used": card_selector,
        "selector_counts": counts,
        "item_count": len(items),
        "items": items,
    }