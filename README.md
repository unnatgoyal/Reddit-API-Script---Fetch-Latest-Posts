# Reddit API Script
This script authenticates with the Reddit API and fetches the latest 5 posts from a specified subreddit.
## Installation
1. Install Python (if not already installed).
2. Install the required dependencies using:
 ```sh
 pip install praw python-dotenv
 ```
## Setup
1. Create a `.env` file in the project directory and add your Reddit API credentials:
 ```sh
 REDDIT_CLIENT_ID=your_client_id
 REDDIT_CLIENT_SECRET=your_client_secret
 REDDIT_USER_AGENT=your_custom_user_agent
 ```
## Usage
1. Run the script using:
 ```sh
 python reddit_fetch.py
 ```
2. Enter the subreddit name when prompted.
3. The script will display the latest 5 posts with their title, author, upvote count, and URL.
## Example Output
```
Successfully authenticated with Reddit API!
Enter subreddit name (e.g., python): technology
Fetching 5 latest posts from r/technology...

Title: AI is revolutionizing the industry
 Author: tech_guru
 Upvotes: 1050
 URL: https://www.reddit.com/r/technology/post1

Title: New tech trends in 2025
 Author: future_visionary
 Upvotes: 875
 URL: https://www.reddit.com/r/technology/post2
```
## Notes
- Ensure that your Reddit API credentials are correct.
- If you encounter errors, check API rate limits and subreddit availability.
