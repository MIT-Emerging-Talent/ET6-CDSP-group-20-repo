#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Imports
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer

# Colors for datasets
COLORS = {
    "Conversational": "rgba(0, 128, 128, 0.8)",  # Teal
    "Baseline": "rgba(255, 165, 0, 0.75)",  # Soft Orange
}

# Themes to analyze
THEMES_TO_ANALYZE = [
    "AI Performance & Quality",
    "Monetization & Value",
    "Technical Performance",
]


def get_top_tfidf_words(documents, top_n=15):
    """Compute top N TF-IDF scoring words or phrases from a list/series of documents."""
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2), max_features=5000, stop_words="english"
    )
    tfidf_matrix = vectorizer.fit_transform(documents)
    avg_tfidf = tfidf_matrix.mean(axis=0).A1
    terms = vectorizer.get_feature_names_out()
    scores_df = pd.DataFrame({"term": terms, "tfidf": avg_tfidf})
    return scores_df.sort_values(by="tfidf", ascending=False).head(top_n)


def plot_pain_words_bar(top_pain_words, theme, dataset_name, color):
    """Plot a horizontal bar chart of pain words TF-IDF scores using Plotly Express."""
    fig = px.bar(
        top_pain_words.sort_values("tfidf", ascending=True),
        x="tfidf",
        y="term",
        orientation="h",
        title=f"Top Pain Words in '{theme}' - {dataset_name} Dataset (Most Negative Reviews)",
        labels={"tfidf": "TF-IDF Score", "term": "Pain Word / Phrase"},
        color_discrete_sequence=[color],
    )
    fig.update_layout(yaxis=dict(tickfont=dict(size=12)))
    fig.show()


# Load datasets
conv_df = pd.read_csv(
    r"3_data_exploration/conversational_apps_themed_and_scored.csv"
).dropna(subset=["review_text"])
base_df = pd.read_csv(r"3_data_exploration/baseline_app_themed_and_scored.csv").dropna(
    subset=["review_text"]
)

print(f"Conversational dataset shape: {conv_df.shape}")
print(f"Baseline dataset shape: {base_df.shape}")
print("Conversational Themes:", conv_df["theme"].unique())
print("Baseline Themes:", base_df["theme"].unique())

# Analyze themes
for theme in THEMES_TO_ANALYZE:
    print(f"\n=== Analyzing Theme: {theme} ===")
    for ds_name, dataset in [("Conversational", conv_df), ("Baseline", base_df)]:
        theme_reviews = dataset[dataset["theme"] == theme]

        if theme_reviews.empty:
            print(f"No reviews found for theme '{theme}' in {ds_name} dataset.")
            continue

        sentiment_cutoff = theme_reviews["sentiment_score"].quantile(0.25)
        neg_reviews = theme_reviews[
            theme_reviews["sentiment_score"] <= sentiment_cutoff
        ]

        if neg_reviews.empty:
            print(
                f"No negative reviews (bottom 25%) found for theme '{theme}' in {ds_name} dataset."
            )
            continue

        top_pain_words = get_top_tfidf_words(neg_reviews["review_text"], top_n=15)
        plot_pain_words_bar(top_pain_words, theme, ds_name, COLORS[ds_name])

# Focus: Monetization & Value
conv_monet = conv_df[conv_df["theme"] == "Monetization & Value"]
conv_monet_neg = conv_monet[
    conv_monet["sentiment_score"] <= conv_monet["sentiment_score"].quantile(0.25)
]

base_monet = base_df[base_df["theme"] == "Monetization & Value"]
base_monet_neg = base_monet[
    base_monet["sentiment_score"] <= base_monet["sentiment_score"].quantile(0.25)
]

# TF-IDF scores
conv_pain = get_top_tfidf_words(conv_monet_neg["review_text"], top_n=15)
conv_pain["dataset"] = "Conversational"

base_pain = get_top_tfidf_words(base_monet_neg["review_text"], top_n=15)
base_pain["dataset"] = "Baseline"

# Combine and sort
combined = pd.concat([conv_pain, base_pain])
combined_sorted = combined.sort_values(by="tfidf", ascending=True)

# Plot comparison chart
fig = px.bar(
    combined_sorted,
    x="tfidf",
    y="term",
    color="dataset",
    orientation="h",
    barmode="group",
    title=(
        "Emotional Fingerprint Comparison: 'Monetization & Value'"
        "<br><sub>Conversational vs Baseline Apps</sub>"
    ),
    height=700,
    color_discrete_map=COLORS,
    labels={
        "tfidf": "TF-IDF Score (Pain Word Importance)",
        "term": "Pain Word / Phrase",
        "dataset": "App Type",
    },
)

fig.update_traces(
    marker_line_width=0.5,
    marker_line_color="rgba(0,0,0,0.1)",
    hovertemplate="<b>%{y}</b><br>%{x:.4f} TF-IDF<br>%{color}<extra></extra>",
)

fig.update_layout(
    font=dict(family="Segoe UI", size=14),
    title_font=dict(size=22),
    yaxis=dict(
        categoryorder="total ascending",
        tickfont=dict(size=13),
        gridcolor="rgba(200,200,200,0.1)",
    ),
    xaxis=dict(
        tickfont=dict(size=13),
        gridcolor="rgba(200,200,200,0.2)",
    ),
    legend=dict(
        title=None,
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02,
        font=dict(size=13),
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=100, r=120, t=90, b=60),
)

fig.show()
