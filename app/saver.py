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

    new_hrefs = {article["href"] for article in data.get("articles", []) if article.get("href")}

    for existing_run in existing_data:
        existing_hrefs = {
            article["href"]
            for article in existing_run.get("articles", [])
            if article.get("href")
        }

        if new_hrefs == existing_hrefs:
            print("Skipped save: this scrape run already exists.")
            return

    existing_data.append(data)

    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=2)

    print("Saved new scrape run.")