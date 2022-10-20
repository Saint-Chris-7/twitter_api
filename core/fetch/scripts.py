import tweepy
from django.conf import Settings

# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

# Create API object


# Create a tweet

api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


"""
  get tweets on the feed,
  only last 20
"""
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

"""
  methods for tweeting
"""
# api.update_status("Test tweet from Tweepy Python")



#api key:   vmvWDivnn4cUFkcqCj6ITOWSD
#ape key secret:  HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc


#bearer token:  AAAAAAAAAAAAAAAAAAAAACxBiQEAAAAAw775%2BDw540nuGdu1N3l3rW0zaTM%3D8mzEIFaQvSZNe026RnMiTauNdqW6Bf0uVe9g6hmmIzqSBeRKQG


#access token: 3430467803-e2hH1srETYMvwB3TN2Wq9BK9WweltiRhSSnAzSP
#acces token secret: 2itZtjFdhPTBm91oxDgvCywTAlA0VljhFlO2JaCqjVzmu
