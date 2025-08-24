# scripts/scrape_google_play.py

import os

import pandas as pd
from google_play_scraper import Sort, reviews

print("--- Google Play Scraper ---")

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
    "Wysa": "bot.wysa.ai",
    "Replika": "ai.replika.app",
    "Youper": "br.com.youper",
    "Woebot": "com.woebot",
    "Calm": "com.calm.android",
}

REVIEWS_TO_SCRAPE_PER_APP = 10000  # Adjust as needed

# Save raw data to 1_datasets/all_datasets/raw_data
OUTPUT_PATH = os.path.join(REPO_ROOT, "1_datasets", "all_datasets", "raw_data")
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- Scraping Loop ---
for app_name, app_id in APPS_TO_SCRAPE.items():
    print(f"\nScraping: {app_name} ({app_id})")

    try:
        result, _ = reviews(
            app_id, lang="en", sort=Sort.NEWEST, count=REVIEWS_TO_SCRAPE_PER_APP
        )

        if not result:
            print(f"No reviews found for {app_name}.")
            continue

        print(f"Scraped {len(result)} raw reviews for {app_name}.")

        df = pd.DataFrame(result)

        # Save the raw data with a clear filename
        output_file = os.path.join(
            OUTPUT_PATH, f"{app_name.lower()}_google_play_raw.csv"
        )
        df.to_csv(output_file, index=False)
        print(f"Saved raw data to {output_file}")

    except Exception as e:
        print(f"An error occurred while scraping {app_name}: {e}")

print("\n--- Google Play scraping complete. ---")
