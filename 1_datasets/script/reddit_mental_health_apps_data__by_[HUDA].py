import hashlib
import time
import pandas as pd
import praw
import prawcore

# === YOUR Reddit API credentials ===
reddit = praw.Reddit(
    client_id="wG0FLf94gXnCc4ssiA9DpQ",
    client_secret="9mo6X-sfFW4T81DlbMWCR0kRutMhag",
    user_agent="Scraper by u/Equal_Negotiation417",
    username="Equal_Negotiation417",
    password="i]dg1ifm2",
)


# === Settings ===
target_keywords = ["wysa", "replika", "calm"]
subreddits_to_search = [
    "mentalhealth",
    "Anxiety",
    "lonely",
    "depression",
    "socialanxiety",
    "selfimprovement",
]
data = []
seen_hashes = set()  # Prevent duplicates

print("🚀 Starting Reddit scraping...\n")

# === Main scraping loop ===
for subreddit_name in subreddits_to_search:
    subreddit = reddit.subreddit(subreddit_name)
    print(f"🔍 Searching in r/{subreddit_name}...")

    for keyword in target_keywords:
        query = f"title:{keyword} OR selftext:{keyword}"
        print(f"   ➤ Searching for '{keyword}' (limit: 200)...")
        time.sleep(3)  # Wait between queries

        try:
            for post in subreddit.search(query, sort="new", limit=200):
                post_title = post.title
                post_body = post.selftext
                source = "Reddit"
                app_name = keyword.capitalize()

                if not post_body.strip():
                    continue  # Skip empty posts

                # Create hash to prevent duplicates
                content_hash = hashlib.md5(
                    (post_title + post_body).encode("utf-8")
                ).hexdigest()
                if content_hash in seen_hashes:
                    continue
                seen_hashes.add(content_hash)

                try:
                    post.comments.replace_more(limit=0)
                    time.sleep(1)  # Pause after fetching comments

                    for comment in post.comments[:3]:  # Top 3 comments
                        comment_body = comment.body
                        data.append(
                            {
                                "app_name": app_name,
                                "subreddit": subreddit_name,
                                "post_title": post_title,
                                "post_body": post_body,
                                "comment_body": comment_body,
                                "source": source,
                            }
                        )

                except prawcore.exceptions.TooManyRequests:
                    print(
                        "⚠️ Reddit rate limit hit while fetching comments. Waiting 60 seconds..."
                    )
                    time.sleep(60)
                    continue

        except prawcore.exceptions.TooManyRequests:
            print("⏳ Reddit rate limit hit while searching. Waiting 60 seconds...")
            time.sleep(60)
            continue

print(f"\n✅ Finished scraping. Total rows collected: {len(data)}")

# === Save to Excel ===
df = pd.DataFrame(data)
df.to_excel("reddit_mental_health_apps.xlsx", index=False)
print("📁 Data saved to 'reddit_mental_health_apps.xlsx'")
