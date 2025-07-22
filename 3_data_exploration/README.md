# Data Exploration
___

## Notebooks Overview

### 1. `Conversational_Analysis.ipynb`

* **Input Dataset:** `conversational_apps_processed.csv`
* **Exploration Summary:** This notebook conducts a deep exploratory analysis of
the user complaints for our set of conversational AI apps. The exploration includes:
  * **Theme Discovery:** Using the BERTopic model to identify the core themes of
  user dissatisfaction.
  * **Frequency Visualization:** Charting the distribution of these themes to see
  which problems are most common.
  * **Emotional Analysis:** Using a Transformer-based sentiment model to explore
  the emotional intensity of each complaint theme.
  * **Temporal Exploration:** A time series analysis to visualize how complaint volumes
  for different themes have changed over time, correlated with real-world events.
* **Key Exploratory Finding:** A multi-faceted "complaint fingerprint" was discovered,
with major themes around Monetization, Technical Performance, and unique failures
of AI Conversational Quality. A dramatic spike in
complaints was identified around February 2023.

### 2. `Baseline_Analysis.ipynb`

* **Input Dataset:** `baseline_app_processed.csv`
* **Exploration Summary:** This notebook performs a parallel exploration on our
baseline app (Calm)to establish a "control group" for comparison. It applies the
exact same exploratory techniques as the conversational notebook:
  * BERTopic theme discovery.
  * Frequency and sentiment visualizations.
  * Time series exploration of complaint volume.
* **Key Exploratory Finding:** The complaint fingerprint for the baseline app is
 overwhelmingly dominated by the **Monetization & Value** theme. Crucially, the
 AI-specific failure themes found in the conversational apps are completely absent,
 providing a stark point of contrast.

### 3. `Comparative_Analysis.ipynb`

* **Purpose:** This notebook serves as the primary synthesis of our project's findings.
* **Methodology:** It loads the themed and scored data from both the conversational
and baseline app analyses and creates a series of powerful, direct-comparison visualizations.
* **Key Finding:** This analysis provides definitive, data-driven evidence of the
"Conversational AI Tax." It visually demonstrates that conversational apps have
a fundamentally different "complaint fingerprint" than traditional apps, with
unique and significant failure modes related to AI performance, memory, and personality.

### Supporting Explorations

* **`App_Specific_Breakdown_Ayham.ipynb`** *(To be added)*
* **`LDA_Validation_Huda.ipynb`** *(To be added)*
* **`Emotional_Fingerprint_Zizi.ipynb`** *(To be added)*
