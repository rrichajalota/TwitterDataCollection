try:
	import json
except ImportError:
	import simplejson as json

tweets_filename = 'twitter_stream_1000tweets.txt'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
	try:
		#convert each line into a json object
		tweet = json.loads(line.strip())
		if 'text' in tweet: #only messages contain 'text' field in a tweet
			print tweet['id'] #tweet's id
			print tweet['created_at'] #when the tweet posted
			print tweet['text'] #content 
			print tweet['user']['id']  # id of the user who posted it
			print tweet['user']['name'] #name of the user
			print tweet['user']['screen_name'] #name of the user account

			hashtags= []
			for hashtag in tweet['entities']['hashtags']:
				hashtags.append(hashtag['text'])
			print hashtags

	except:
		continue