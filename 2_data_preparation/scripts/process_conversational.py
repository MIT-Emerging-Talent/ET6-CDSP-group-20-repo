import pandas as pd
import glob
import os
from datetime import datetime
from langdetect import detect, LangDetectException
import numpy as np

print("--- Starting Focused Preprocessing for CONVERSATIONAL APPS (v_final) ---")

# --- 1. Configuration ---
RAW_DATA_PATH = "../0_datasets/raw"
PROCESSED_DATA_PATH = "../data/"
CONVERSATIONAL_APPS_FILES = ["wysa", "replika", "woebot", "youper"]

# --- 2. Load Conversational App Files ---
all_files = glob.glob(os.path.join(RAW_DATA_PATH, "*.csv"))
conv_files = [
    f for f in all_files if any(app in f.lower() for app in CONVERSATIONAL_APPS_FILES)
]
if not conv_files:
    print("ERROR: No conversational app files found.")
    exit()

print(f"Found {len(conv_files)} conversational app files to process.")

# --- 3. Load, Standardize, and Combine (NEW ROBUST METHOD) ---
cleaned_dfs = []
for f in conv_files:
    # Load one file at a time
    raw_df = pd.read_csv(f, low_memory=False)

    # Create a new, clean DataFrame for this file
    clean_df = pd.DataFrame()

    # --- Define our standard columns and find the raw data for them ---

    # For 'text' column
    text_candidates = ["review_text", "content", "review", "title", "body"]
    for col in text_candidates:
        if col in raw_df.columns:
            clean_df["text"] = raw_df[col]
            break  # Stop after finding the first one

    # For 'rating' column
    rating_candidates = ["rating", "score"]
    for col in rating_candidates:
        if col in raw_df.columns:
            clean_df["rating"] = raw_df[col]
            break

    # For 'date' column
    date_candidates = ["review_date", "at", "date"]
    for col in date_candidates:
        if col in raw_df.columns:
            clean_df["date"] = raw_df[col]
            break

    # For 'user' column
    user_candidates = ["user_name", "userName"]
    for col in user_candidates:
        if col in raw_df.columns:
            clean_df["user"] = raw_df[col]
            break

    # If any essential column is still missing, add it with nulls
    for std_col in ["text", "rating", "date", "user"]:
        if std_col not in clean_df.columns:
            clean_df[std_col] = np.nan

    cleaned_dfs.append(clean_df)

# Now, combine the list of clean, standardized DataFrames
df_master = pd.concat(cleaned_dfs, ignore_index=True)
print(f"Loaded and standardized {len(df_master)} total rows.")


# --- 4. Clean, De-duplicate, and Process ---
# The rest of the script should now work perfectly because df_master has a clean schema.

# De-duplicate
df_master.dropna(subset=["text", "user"], inplace=True)
df_master["text_short"] = df_master["text"].astype(str).str.slice(0, 250)
df_master.drop_duplicates(
    subset=["user", "date", "text_short"], keep="first", inplace=True
)
df_master.drop(columns=["text_short"], inplace=True)
print(f"After de-duplication: {len(df_master)} rows.")

# In process_conversational_final.py

# ... (after de-duplication) ...

# --- Language Detection ---
print("Detecting language...")


# ** THE FIX IS HERE: A ROBUST, ERROR-HANDLING FUNCTION **
def safe_detect(text):
    """
    A wrapper around the langdetect function to handle errors gracefully.
    """
    # First, check if the text is a valid string and has some content
    if not isinstance(text, str) or len(text.strip()) < 10:
        return "unknown"

    try:
        # If it's a valid string, try to detect the language
        return detect(text)
    except LangDetectException:
        # If langdetect fails, label it as 'unknown' and continue
        return "unknown"


# Apply our new, safe function to the 'text' column
df_master["lang"] = df_master["text"].astype(str).str.lower().apply(safe_detect)

df_english = df_master[df_master["lang"] == "en"].copy()
print(f"Filtered for English: {len(df_english)} rows.")


# --- The rest of the script continues from here ---
# (Final Filtering, Schema, Saving) ...

# Final Filtering
df_english["date"] = pd.to_datetime(df_english["date"], errors="coerce")
df_english["rating"] = pd.to_numeric(df_english["rating"], errors="coerce")
df_english.dropna(subset=["rating"], inplace=True)

date_condition = (df_english["date"] >= datetime(2022, 1, 1)) | (
    df_english["date"].isna()
)
rating_condition = df_english["rating"].isin([1, 2, 3])
df_final = df_english[date_condition & rating_condition]
print(f"After final filtering for date and rating: {len(df_final)} rows remain.")

# --- 5. Finalize Schema and Save ---
df_final.rename(columns={"text": "review_text", "user": "user_name"}, inplace=True)
FINAL_COLUMNS = ["user_name", "review_text", "rating", "date"]
df_final = df_final[FINAL_COLUMNS]

os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
output_path = os.path.join(PROCESSED_DATA_PATH, "conversational_apps_dataset.csv")
df_final.to_csv(output_path, index=False)

print(f"\nSUCCESS! Saved final processed file to: {output_path}")
print(f"Total final rows: {len(df_final)}")
print("\n--- Script Finished ---")
