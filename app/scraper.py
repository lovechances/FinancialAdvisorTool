def scrape_visible_text(page) -> dict:
    title = page.title()

    body_text = page.locator("body").inner_text()

    words = body_text.split()
    preview = " ".join(words[:200])

    return {
        "title": title,
        "word_count": len(words),
        "preview": preview,
    }