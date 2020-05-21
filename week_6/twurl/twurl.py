import urllib.request, urllib.parse, urllib.error
import tweepy
from week_6 import hidden

def augment(url, parameters):
    secrets = hidden.oauth()
    auth = tweepy.OAuthHandler(secrets['consumer_key'],secrets['consumer_key_secret'])
    auth.set_access_token(secrets['token_key'],secrets['token_key_secret'])
    api = tweepy.API(auth)


