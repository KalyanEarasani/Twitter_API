import twitter

def get_twitter_api(access_token, access_token_secret):
    api = twitter.Api(
        consumer_key='your_consumer_key',
        consumer_secret='your_consumer_secret',
        access_token_key=access_token,
        access_token_secret=access_token_secret
    )
    return api
