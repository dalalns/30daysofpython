import os
import tweepy as tw
import pandas as pd
#https://developer.twitter.com/en/apps/15969080
#https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/get-and-use-twitter-data-in-python/
consumer_key= 'jPupcEPJxn3gRABlsNnVF6eTD'
consumer_secret= 'KWfjF6jiKzccG7VvQPNjCBrhxPjRJTRWjYXJ0wG4O4EUKFrxvN'
access_token= '99484419-BewhNoykNeIGz5e3RqdrrcH6ILZNjAKani5OUenvx'
access_token_secret= 'dOMSXQ9BpkBa5W43Q8G2kbfHa16MSrlhcCxAldeInU9VA'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#api.update_status("twitting from python")

search_words = "#TapseePannu"
date_since = "2019-11-24"

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)

print(tweets)

for tweet in tweets:
	print(tweet.text)

