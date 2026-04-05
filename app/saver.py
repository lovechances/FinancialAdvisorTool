import os
import json


def save(data: dict):
    folder = "data"
    os.makedirs(folder, exist_ok=True)

    file_path = f"{folder}/data.json"

    existing_data = []

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []

    if not isinstance(existing_data, list):
        existing_data = [existing_data]

    # build one big set of all existing hrefs
    existing_hrefs = set()

    for existing_run in existing_data:
        for article in existing_run.get("articles", []):
            href = article.get("href")
            if href:
                existing_hrefs.add(href)

    # keep only brand new articles from this run
    cleaned_articles = []

    for article in data.get("articles", []):
        href = article.get("href")
        if href and href not in existing_hrefs:
            cleaned_articles.append(article)

    # if nothing new, skip save
    if not cleaned_articles:
        print("Skipped save: no new articles found.")
        return

    # copy the run metadata, but replace articles with only new ones
    cleaned_run = {
        "source_section": data.get("source_section"),
        "source_selector": data.get("source_selector"),
        "source_count": len(cleaned_articles),
        "articles": cleaned_articles,
    }

    existing_data.append(cleaned_run)

    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=2)

    print("Saved new scrape run.")