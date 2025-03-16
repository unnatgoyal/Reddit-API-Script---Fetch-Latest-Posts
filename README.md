# Reddit API Fetch Script
This script connects to the Reddit API using OAuth authentication and retrieves the 5 latest posts from a specified subreddit. It prints each post's title, author, upvote count, and URL.

Installation

Install Python (if not already installed).

Install the required dependencies using:

pip install praw python-dotenv

Setup

Create a .env file in the project directory and add your Reddit API credentials:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_custom_user_agent

Usage

Run the script using:

python reddit_fetch.py

Enter the subreddit name when prompted.

The script will display the latest 5 posts with their title, author, upvote count, and URL.

Example Output

✅ Successfully authenticated with Reddit API!
Enter subreddit name (e.g., python): technology
📢 Fetching 5 latest posts from r/technology...

      🔹 Title: AI is revolutionizing the industry
         Author: tech_guru
         Upvotes: 1050
         URL: https://www.reddit.com/r/technology/post1

      🔹 Title: New tech trends in 2025
         Author: future_visionary
         Upvotes: 875
         URL: https://www.reddit.com/r/technology/post2

Notes

Ensure that your Reddit API credentials are correct.

If you encounter errors, check API rate limits and subreddit availability.


