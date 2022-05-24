import praw
import os
from dotenv import load_dotenv

def setup_reddit():
    load_dotenv()

    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    USER_AGENT = os.getenv('USER_AGENT')

    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

    return reddit