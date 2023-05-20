import praw
import openai

# Reddit API credentials
reddit_client_id = '8IvnbB8h3jYOA6XUVhlz2g'
reddit_client_secret = 'zMch1-6NR1nIT_PCgGJOWEFu5_23_w'
reddit_user_agent = 'myapp'

# OpenAI API credentials
openai_api_key = 'Your_API_Key'

# Initialize Reddit API
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# Set up OpenAI API
openai.api_key = openai_api_key

# Subreddit to analyze
subreddit_name = 'bitcoin'

# Number of posts to fetch
num_posts = 100

# Fetch posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit=num_posts)

# Extract titles and store them in a list
post_titles = [post.title for post in posts]


# Convert list of titles to a single string
input_text = '\n'.join(post_titles)

# Call the OpenAI API for summarization
response = openai.Completion.create(
  engine='text-davinci-003',
  prompt=input_text,
  max_tokens=100,
  temperature=0.5,
  n=1,
  stop=None,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Extract the generated summary
summary = response.choices[0].text.strip()

# Print the summary
print("Summary of trends in", subreddit_name)
print(summary)
print(post_titles)
