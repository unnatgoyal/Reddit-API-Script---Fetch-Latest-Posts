import os
import praw
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API credentials
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Debugging: Check if values are loading correctly
if not CLIENT_ID or not CLIENT_SECRET or not USER_AGENT:
    print("❌ ERROR: Missing environment variables. Check your .env file!")
    exit()

# Authenticate with Reddit API
try:
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    print("✅ Successfully authenticated with Reddit API!\n")

except Exception as e:
    print(f"❌ Authentication failed: {e}")
    exit()

# Function to fetch latest 5 posts from a subreddit
def fetch_latest_posts(subreddit_name):
    try:
        print(f"📢 Fetching 5 latest posts from r/{subreddit_name}...\n")
        subreddit = reddit.subreddit(subreddit_name)

        for post in subreddit.new(limit=5):  # Fetch latest 5 posts
            print(f"🔹 Title: {post.title}")
            print(f"   Author: {post.author}")
            print(f"   Upvotes: {post.score}")
            print(f"   URL: {post.url}\n")

    except Exception as e:
        print(f"❌ Error fetching posts: {e}")

# Run the function for a specific subreddit
if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name : ")
    fetch_latest_posts(subreddit_name)
