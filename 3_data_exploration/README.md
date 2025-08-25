# Data Exploration

___

## Notebooks Overview

### 1. `Conversational_Analysis.ipynb`

* **Input Dataset:** `conversational_apps_dataset.csv`
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

* **Input Dataset:** `baseline_app_dataset.csv`
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

🔹 **Aziz Azizi**

* **emotional_fingerprint.ipynb**  

  Description: Exploring and comparing negative review "pain words" across major
  complaint themes in both Conversational and Baseline mental health app datasets
  using TF-IDF. Includes visualizations highlighting the emotional fingerprints
  of user frustrations.

  Methodology:  
  * Uses sentiment analysis (VADER) to identify the most negative reviews per
  theme.  
  * Applies TF-IDF vectorization to extract the top weighted words and phrases
  driving negative sentiment ("pain words").  
  * Visualizes findings with interactive bar charts using Plotly.
  
🔹 **Ayham**

* **`app-based-comparative-analysis4.ipynb`**  

  Description: This notebook performs an app-specific comparative analysis of
   the four conversational AI apps to assess their failure modes
    and answer these questions :

   "Are the apps failing in the same way"

   "How intese the complaints are"

   "Are the apps failing at the same rate" (Time series analysis)

  Methodology:
  * Loads individual CSV files of user reviews per app.
  * Combines datasets and cleans textual data.
  * Uses **VADER** sentiment analysis to isolate negative (complaint) reviews.
  * Applies **BERTopic** for topic modeling on complaints.
  * Maps granular topics to five core failure themes.
  * Generates:
    * A stacked bar chart comparing failure themes across apps.
    * A box plot visualizing complaint intensity per app.
    * A time series line chart tracking normalized failure rates over time.

🔹 **Huda**

### Summary of NLP Analysis with LDA and Sentiment

* **Input Dataset**

The analysis utilized a dataset named `conversational_apps_dataset.csv`,
containing user reviews of conversational applications, specifically those
designed for mental health support. The primary data point for analysis was
the `review_text` column, which contained the raw textual feedback provided by users.

* **Exploration Summary**

Prior to conducting the topic modeling and sentiment analysis, the following steps
were performed as part of the data exploration and preparation phase:

1. **Text Preprocessing**
2. **Handling of Empty Reviews**
3. **Text Vectorization**
4. **LDA Model Application**
5. **Topic Labeling**

* **Key Exploratory Findings**

In summary, the analysis highlights that while mental health chatbots are
successful in providing positive experiences for a notable user base,
significant challenges remain in areas concerning the naturalness and
appropriateness of conversational responses, as well as technical and
billing-related issues.

## Additional Files (saved in the 1_datasets\all_datasets)

* `baseline_app_themed_and_scored.csv` — Baseline mental health app reviews with
theme and sentiment scores.
* `conversational_apps_themed_and_scored.csv` — Conversational mental health app
reviews with theme and sentiment scores.
