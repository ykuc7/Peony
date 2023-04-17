import os
import pprint

import dotenv
import tweepy

dotenv.load_dotenv()


def create_twitter_client():
    # credential
    consumer_key = os.environ['TW_CONSUMER_KEY']
    consumer_secret = os.environ['TW_CONSUMER_SECRET']
    access_token = os.environ['TW_ACCESS_TOKEN']
    access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']
    bearer_token = os.environ['TW_BEARER_TOKEN']
    client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret,
                           bearer_token=bearer_token)
    return client


if __name__ == "__main__":
    client = create_twitter_client()
    me = client.get_me()
    pprint.pprint(me)
