import json 
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contain the user credentials to access Twitter API 
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_SECRET = 'ACCESS_SECRET'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

#Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

#get a sample of public data flowing through Twitter
iterator= twitter_stream.statuses.sample()

'''
Print each tweet in the stream to the screen. Here 
we set it to stop after getting 1000. Stopping is optional. We can continue
running the twitter API to collect data for days.
'''
tweet_count= 1000
for tweet in iterator:
	tweet_count -= 1         #Twitter Python Tool wraps the data returned by Twitter
	print json.dumps(tweet)	 #as a TwitterDictResponse object. We convert it back to the 
							 #JSON format to print
	if tweet_count <= 0:
		break

'''
Run the file in terminal and save the data in a text file.
$ python twitter_streaming.py > twitter_stream_1000tweets.txt
'''