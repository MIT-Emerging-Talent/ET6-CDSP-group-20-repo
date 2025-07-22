# Data Preparation: Scripts Summary

This folder contains the Python scripts used to process our raw, scraped user
reviews into clean, analysis-ready datasets.

## Scripts Overview

### 1. `process_conversational.py`

* **Input Dataset(s):** Reads all raw `.csv` files containing "wysa," "replika,"
"woebot," or "youper" from the `/0_datasets/raw/` folder.
* **Processing Steps:** This script performs a multi-step pipeline including
schema standardization, de-duplication of overlapping scrapes, language detection
to filter for English reviews, and filtering for 1-3 star ratings since 2022.
* **Output Dataset(s):** Writes a single, clean file named `conversational_apps_processed.csv`
to the `/0_datasets/` folder.

### 2. `process_baseline.py`

* **Input Dataset(s):** Reads all raw `.csv` files containing "calm" from the `/0_datasets/raw/`
folder.
* **Processing Steps:** Applies the exact same cleaning, de-duplication, and
filtering pipelineas the conversational script to ensure methodological consistency.
* **Output Dataset(s):** Writes a single, clean file named
`baseline_app_processed.csv` to the `/0_datasets/` folder.

**Note:** The output datasets are the direct input for the notebooks in the
`3_data_exploration` and `4_data_analysis` folders.
