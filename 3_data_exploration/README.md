# Data Exploration

This folder contains individual exploratory and deep dive notebooks
from the team members, showcasing different angles and validations of our
mental health app reviews data.

___

## Notebooks

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

## Additional Files

* `baseline_app_themed_and_scored.csv` — Baseline mental health app reviews with
theme and sentiment scores.
* `conversational_apps_themed_and_scored.csv` — Conversational mental health app
reviews with theme and sentiment scores.
