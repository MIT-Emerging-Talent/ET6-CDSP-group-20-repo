# Methods

This document explains the methods, tools, and processes used in our project
so that others can understand and reproduce our work.

___

## 1. Data Source

* **Dataset:** MHARD (Mental Health App Reviews Dataset) from Kaggle.

* **Focus:** Conversational mental health apps, especially Calm, compared with
other baseline apps.

* **Data format:** Play store reviews in CSV format, including review text, rating,
  and metadata.

## 2. Data Preparation

We cleaned and pre-processed the dataset before applying any analysis:

* Removed duplicates and irrelevant entries.

* Lowercased and stripped punctuation.

* Applied TF-IDF vectorization for text representation.

* Organized reviews into baseline apps vs conversational apps subsets.

## 3. Sentiment Analysis

We used **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to analyze
sentiment of each review:

* Outputs: positive, negative, neutral, compound score.

* Compound scores were used to categorize reviews into positive, neutral,
or negative sentiment.

This helped us see how users emotionally react to chatbot support compared to baseline apps.

## 4. Topic Modeling

We used BERTopic for topic modeling:

* BERTopic builds interpretable topics using transformer embeddings + clustering.

* Each review was assigned to a topic cluster.

* Topics were named using representative keywords (e.g., AI Performance &
  Quality, Emotional Support, Privacy Concerns).

* This helped us identify major themes in user feedback.

## 5. Thematic + Emotional Fingerprint

To go beyond generic sentiment, we:

* Filtered reviews by theme (e.g., AI Performance & Quality).

* Extracted negative/highly emotional words using TF-IDF + sentiment scores.

* Built “Emotional Fingerprints” of negative themes (e.g., words like
  useless, fake, disappointing cluster around AI performance).

* Visualized results with word clouds and tables.

## 6. Reproducibility

* Steps are divided by folder:

  * 2_data_preparation/ → cleaning & TF-IDF

  * 3_data_exploration/ → VADER sentiment analysis

  * 4_data_analysis/ → BERTopic + Emotional Fingerprint

___

## 🛠 Tools and Libraries

* Data Collection

  * app-store-scraper (0.3.5) → Scraped iOS app reviews.

  * google-play-scraper (1.2.7) → Scraped Android app reviews.

  * praw (7.8.1), psaw (0.1.0) → Collected Reddit posts and comments for extra
  community insights.

* Data Processing & Preparation

  * pandas (2.3.2), numpy (1.26.4) → Data cleaning, manipulation, and preprocessing.

  * regex (2025.7.34), nltk (3.9.1), textblob (0.19.0), langdetect (1.0.9) →
  Text preprocessing, tokenization, stopword removal, language detection.

  * openpyxl (3.1.5) → Handle Excel datasets.

  * wordcloud (1.9.4) → Generate visual word clouds of user sentiments.

* Analysis & Modeling

  * VADER (nltk integration) → Sentiment analysis (positive/negative/neutral
    scores).

  * BERTopic (0.16.0) → Topic modeling on mental health chatbot reviews.

  * UMAP (0.5.7) + HDBSCAN (0.8.33) → Dimensionality reduction + clustering.

  * Sentence-Transformers (5.1.0) + Transformers (4.55.3) → Embeddings for
    BERTopic.

  * scikit-learn (1.3.2) → Machine learning utilities (TF-IDF, preprocessing).

  * matplotlib (3.10.5), seaborn (0.13.2), plotly (6.3.0) → Data visualization.

* Environment & Utilities

  * Jupyter Notebook (ipykernel, ipython, etc.) → Interactive development.

  * python-dotenv (1.1.1) → Manage environment variables (API keys).

  * tqdm (4.67.1) → Progress bars during scraping and analysis.
