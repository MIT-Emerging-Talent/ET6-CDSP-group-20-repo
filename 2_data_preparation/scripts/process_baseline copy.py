import glob
import os
from datetime import datetime

import numpy as np
import pandas as pd
from langdetect import LangDetectException, detect

print("--- Starting Focused Preprocessing for BASELINE APP (Calm) ---")

# --- 1. Detect repo root ---
cwd = os.getcwd()
while not os.path.exists(os.path.join(cwd, "1_datasets")):
    parent = os.path.dirname(cwd)
    if parent == cwd:  # reached root of drive
        raise FileNotFoundError("Could not find repo root containing '1_datasets'.")
    cwd = parent

REPO_ROOT = cwd
print(f"Repo root detected at: {REPO_ROOT}")

# --- 2. Define paths ---
RAW_DATA_PATH = os.path.join(REPO_ROOT, "1_datasets", "all_datasets", "raw_data")
PROCESSED_DATA_PATH = os.path.join(REPO_ROOT, "1_datasets", "all_datasets")

# --- 3. Define baseline app names (lowercase) ---
BASELINE_APP_FILES = ["calm"]  # adjust if your files have different keywords

# --- 4. Find and Load ONLY Baseline App Files ---
all_files = glob.glob(os.path.join(RAW_DATA_PATH, "*.csv"))
app_files = [
    f
    for f in all_files
    if any(app in os.path.basename(f).lower() for app in BASELINE_APP_FILES)
]

if not app_files:
    print(
        f"ERROR: No baseline app files ({BASELINE_APP_FILES}) found. Please check your file names and paths."
    )
    exit()

print(f"Found {len(app_files)} baseline app files to process.")

# --- 5. Load, Standardize, and Combine ---
cleaned_dfs = []
for f in app_files:
    raw_df = pd.read_csv(f, low_memory=False)
    clean_df = pd.DataFrame()

    # Standardize text
    text_candidates = ["review_text", "content", "review", "title", "body"]
    for col in text_candidates:
        if col in raw_df.columns:
            clean_df["text"] = raw_df[col]
            break

    # Standardize rating
    rating_candidates = ["rating", "score"]
    for col in rating_candidates:
        if col in raw_df.columns:
            clean_df["rating"] = raw_df[col]
            break

    # Standardize date
    date_candidates = ["review_date", "at", "date"]
    for col in date_candidates:
        if col in raw_df.columns:
            clean_df["date"] = raw_df[col]
            break

    # Standardize user
    user_candidates = ["user_name", "userName"]
    for col in user_candidates:
        if col in raw_df.columns:
            clean_df["user"] = raw_df[col]
            break

    # Fill missing essential columns with NaN
    for std_col in ["text", "rating", "date", "user"]:
        if std_col not in clean_df.columns:
            clean_df[std_col] = np.nan

    cleaned_dfs.append(clean_df)

df_master = pd.concat(cleaned_dfs, ignore_index=True)
print(f"Loaded and standardized {len(df_master)} total rows.")

# --- 6. Clean, De-duplicate, and Process ---
df_master.dropna(subset=["text", "user"], inplace=True)
df_master["text_short"] = df_master["text"].astype(str).str.slice(0, 250)
df_master.drop_duplicates(
    subset=["user", "date", "text_short"], keep="first", inplace=True
)
df_master.drop(columns=["text_short"], inplace=True)
print(f"After de-duplication: {len(df_master)} rows.")

# --- 7. Language Detection ---
print("Detecting language...")


def safe_detect(text):
    if not isinstance(text, str) or len(text.strip()) < 10:
        return "unknown"
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"


df_master["lang"] = df_master["text"].astype(str).str.lower().apply(safe_detect)
df_english = df_master[df_master["lang"] == "en"].copy()
print(f"Filtered for English: {len(df_english)} rows.")

# --- 8. Final Filtering ---
df_english["date"] = pd.to_datetime(df_english["date"], errors="coerce")
df_english["rating"] = pd.to_numeric(df_english["rating"], errors="coerce")
df_english.dropna(subset=["rating"], inplace=True)

date_condition = (df_english["date"] >= datetime(2022, 1, 1)) | (
    df_english["date"].isna()
)
rating_condition = df_english["rating"].isin([1, 2, 3])
df_final = df_english.loc[date_condition & rating_condition]
print(f"After final filtering for date and rating: {len(df_final)} rows remain.")

# --- 9. Finalize Schema and Save ---
df_final = df_final.rename(columns={"text": "review_text", "user": "user_name"})
FINAL_COLUMNS = ["user_name", "review_text", "rating", "date"]
df_final = df_final[FINAL_COLUMNS]

os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
output_path = os.path.join(PROCESSED_DATA_PATH, "baseline_app_dataset.csv")
df_final.to_csv(output_path, index=False)

print(f"\nSUCCESS! Saved final processed file to: {output_path}")
print(f"Total final rows: {len(df_final)}")
print("\n--- Script Finished ---")
