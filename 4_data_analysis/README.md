# Data Analysis: Quantifying the "Conversational AI Tax"

Welcome to the analytical core of our project. This folder contains the scripts
and notebooks that transform raw user feedback into a compelling, data-driven
narrative about the unique challenges of mentalhealth chatbots. Our primary
deliverable is a master analysis notebook that synthesizes multiple advanced
NLP techniques to tell a complete story.

Our entire analytical journey is guided by a central research question:

> *What are the most prevalent themes of user-reported conversational failure in
leading mental health chatbots, and what do these themes reveal about the gap between
user expectations for emotional support and current algorithmic capabilities?*

---

## The Analytical Workflow: A Multi-Model Approach

To answer our question with the highest degree of confidence, we designed a
sophisticated, multi-layered analytical workflow. This ensures our findings
are not an artifact of a single technique but are robust, validated, and deeply contextualized.

### 1. [`The_Conversational_AI_Tax_A_Comparative_Analysis.ipynb`](https://www.kaggle.com/code/sadamhali/the-conversational-ai-tax-a-comparative-analysis)

This is the **master notebook** and the definitive source of truth for our findings.
 It weaves together all stages of the analysis into a single, reproducible narrative.

* **Initial Validation (Classic NLP):** The notebook begins by using traditional
models (`Latent Dirichlet Allocation` & `TextBlob`) to establish a foundational
understanding of the complaint themes. This step acts as a crucial sanity check
and validates our initial hypotheses.

* **Deep Thematic Discovery (BERTopic):** The core of our analysis uses `BERTopic`,
a state-of-the-art topic modeling technique. By leveraging transformer-based sentence
embeddings, this model moves beyond simple word counts to cluster reviews based
on their underlying semantic *meaning*. We train two separate models—one on our
primary corpus of **Conversational Apps** and another on our **Baseline (Calm)**
corpus—to enable a powerful comparative analysis.

* **Emotional Impact Analysis (Transformers):** To measure the *intensity* of user
frustration, we employ a fine-tuned RoBERTa-based sentiment model
(`cardiffnlp/twitter-roberta-base-sentiment-latest`). This allows us to go beyond
*what* users complain about to understand *how deeply* each failure impacts them,
assigning a precise sentiment score to over 30,000 reviews.

* **Temporal & App-Specific Deep Dives:** The analysis is further enriched by
tracking complaint themes over time and breaking them down by individual app,
revealing the direct impact of real-world events and highlighting the unique
failure profiles of different products.

---

## In-Depth Research Findings

Our analysis produced three core findings that, together, paint a vivid picture
of the "Conversational AI Tax."

### Key Finding 1: The "Complaint Fingerprint" is Fundamentally Different

Our most significant finding is the stark contrast in *why* users complain about
conversational AI versus traditional apps. We visualize this as a "Complaint Fingerprint."
For the baseline app, negative reviews are overwhelmingly dominated by
**Monetization & Value**.
For conversational apps, this concern is diluted by the emergence of massive,
new categories of failure.

This chart proves that conversational apps are not just judged as tools, but as
partners, and they are heavily penalized when they fail in that role.

[![The Complaint Fingerprint](https://drive.google.com/uc?export=view&id=15fXNSNaOtpUaqtFdvQPyjZJ6R6wvfJ2D)](https://drive.google.com/uc?export=view&id=15fXNSNaOtpUaqtFdvQPyjZJ6R6wvfJ2D/view?usp=sharing)

### Key Finding 2: A Bad Conversation is More Painful Than a Bad Price

Frequency alone does not tell the whole story. Our "Problem Priority Matrix" plots
the frequency of a complaint theme against its average emotional intensity.

This reveals a critical insight: while **Monetization** is a chronic annoyance,
failures in **AI Performance & Quality** and catastrophic **Technical Performance**
issues are categorized as "Critical Issues"—they are both frequent and deeply
frustrating to the user. This suggests that a broken or "dumb" AI causes more
acute user pain than a high subscription fee.

[![Problem Priority Matrix for Conversational Apps](https://drive.google.com/uc?export=view&id=1mywSjbWWMD7EwrEfIpmqNRWTubE7X9Z9)](https://drive.google.com/file/d/1mywSjbWWMD7EwrEfIpmqNRWTubE7X9Z9/view?usp=sharing)

### Key Finding 3: The "Smoking Gun" - Real-World Events Drive User Backlash

Our time series analysis provides undeniable evidence of the volatility of the
conversational AI user base. The chart below shows the evolution of complaint
themes over time.

The vertical line marks the **February 2023 Replika ERP Update**, a controversial
event that removed romantic features. We can see an immediate, cataclysmic spike
in complaints related to **AI Performance**, **Feature-Specific Issues**, and even
**Monetization** (as users felt they lost a paid feature). This directly links a
corporate product decision to a massive, multi-faceted erosion of user trust and
satisfaction, a phenomenon not observed in the stable trend lines of our baseline
app.

[![Evolution of User Complaints Over Time](https://drive.google.com/uc?export=view&id=1mv3KFTeCk6-0gNL4SCBkR0HdBT6xoi9p)](https://drive.google.com/file/d/1mv3KFTeCk6-0gNL4SCBkR0HdBT6xoi9p/view?usp=sharing)

### Overall Conclusion

The "Conversational AI Tax" is a real and significant burden. The cost of creating
a human-like AI companion is a vast new surface area for product failure. Users
bring deep-seated, human expectations for memory, personality, and empathy to these
digital relationships. Our analysis demonstrates that the gap between these innate
expectations and the current reality of algorithmic capabilities is the primary,
unique, and most emotionally charged driver of user dissatisfaction in the rapidly
growing world of mental health chatbots.
