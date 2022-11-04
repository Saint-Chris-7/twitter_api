import tweepy
from django.conf import settings

# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

# Create API object


# Create a tweet

# api = tweepy.API(auth, wait_on_rate_limit=True)
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


"""
  get tweets on the feed,
  only last 20
"""
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

def my_timeline():
    """
    timeline fn fetch twitter timeline

    returns a list of tweets
    """
    auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
    auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    timeline = api.home_timeline()
    # for tweet in timeline:
    #     print(f"{tweet.user.name} said {tweet.text}")
    return timeline


