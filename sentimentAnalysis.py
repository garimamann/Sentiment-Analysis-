import csv
import tweepy 
from textblob import TextBlob
from tweepy.auth import OAuthHandler

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('SZA')

with open("tweet.csv","w",encoding="utf-8") as f:
	 fieldnames = ['tweet','sentiment']
	 csv_write = csv.writer(f)


	 for result in public_tweets:
	  analysis = TextBlob(result.text)
	  if analysis.sentiment.polarity > 0.5:
	  	lable ="positive"
	  else:
	  	lable = "negative"
	  csv_write.writerow([result.text,analysis.sentiment,lable])
	 
	



