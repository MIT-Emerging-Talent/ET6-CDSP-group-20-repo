# scripts/scrape_apple_app_store.py

import os
import pandas as pd
from app_store_scraper import AppStore

print("--- Apple App Store Scraper ---")

# --- Detect repo root ---
cwd = os.getcwd()
while not os.path.exists(os.path.join(cwd, "1_datasets")):
    parent = os.path.dirname(cwd)
    if parent == cwd:  # reached root of drive
        raise FileNotFoundError("Could not find repo root containing '1_datasets'.")
    cwd = parent
REPO_ROOT = cwd
print(f"Repo root detected at: {REPO_ROOT}")

# --- Configuration ---
APPS_TO_SCRAPE = {
    "Wysa": "wysa-ai-therapist-chat-bot",
    "Replika": "replika-my-ai-friend",
    "Woebot": "woebot-your-self-care-expert",
    "Youper": "youper-cbt-therapy-journal",
    "Calm": "calm",
}

COUNTRIES_TO_SCRAPE = ["us", "gb", "ca", "au", "in"]
REVIEWS_LIMIT_PER_APP = 5000

OUTPUT_PATH = os.path.join(REPO_ROOT, "1_datasets", "all_datasets", "raw_data")
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- Scraping Loop ---
for app_name, app_url_name in APPS_TO_SCRAPE.items():
    print(f"\nScraping: {app_name}")
    all_reviews_for_this_app = []

    for country in COUNTRIES_TO_SCRAPE:
        print(f"  -- Checking country: {country}...")
        try:
            app = AppStore(country=country, app_name=app_url_name)
            app.review(how_many=REVIEWS_LIMIT_PER_APP)

            # Only keep reviews that actually exist
            reviews_found = [r for r in app.reviews if r is not None]
            for review in reviews_found:
                review["country"] = country

            all_reviews_for_this_app.extend(reviews_found)
            print(f"  -- Found {len(reviews_found)} reviews in '{country}'.")

        except Exception as e:
            print(
                f"  -- Could not scrape '{country}' for {app_name}. Skipping. Error: {e}"
            )
            continue

    if not all_reviews_for_this_app:
        print(f"No reviews were found for {app_name} across any countries.")
        continue

    print(f"Total raw reviews scraped for {app_name}: {len(all_reviews_for_this_app)}")

    df = pd.DataFrame(all_reviews_for_this_app)

    output_file = os.path.join(
        OUTPUT_PATH, f"{app_name.lower()}_apple_app_store_raw.csv"
    )
    df.to_csv(output_file, index=False)
    print(f"Saved raw data for {app_name} to {output_file}")

print("\n--- Apple App Store scraping complete. ---")
