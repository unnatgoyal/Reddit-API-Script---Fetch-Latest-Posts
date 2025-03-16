Reddit API Script

📌 Overview



This script interacts with the Reddit API to fetch the latest 5 posts from a given subreddit. It uses OAuth authentication via the praw library to securely connect to Reddit.Installation.

🚀 Features

✅ Authenticate with Reddit API using OAuth.

📥 Fetch the 5 latest posts from a specified subreddit.

📝 Display each post's title, author, upvote count, and URL.



🛠️ Handle authentication failures and API errors gracefully

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

✅Successfully authenticated with Reddit API!
Enter subreddit name : title
📢 Fetching 5 latest posts from r/title...

🔹 Title: Movies
   Author: Itcilis
   Upvotes: 6
   URL: https://www.reddit.com/r/Title/comments/eod06x/movies/

🔹 Title: Title History
   Author: Itcilis
   Upvotes: 6
   URL: https://www.reddit.com/r/Title/comments/ensbp3/title_history/

Notes

Ensure that your Reddit API credentials are correct.

If you encounter errors, check API rate limits and subreddit availability.

