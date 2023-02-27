from datetime import datetime
from app import db
from models import User, Tweet
from auth import get_twitter_api

def sync_user_tweets(user):
    api = get_twitter_api(user.access_token, user.access_token_secret)
    tweets = api.GetHomeTimeline(count=100)

    for tweet in tweets:
        tweet_exists = Tweet.query.filter_by(id=tweet.id).first()

        if not tweet_exists:
            new_tweet = Tweet(
                id=tweet.id,
                text=tweet.text,
                created_at=datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y'),
                user_id=user.id)
