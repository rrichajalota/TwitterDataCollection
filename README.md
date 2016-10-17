# TwitterDataCollection
##### This repo contains python script for streaming twitter data. I followed the tutorial [Social Media & Text Analysis](http://socialmedia-class.org/twittertutorial.html) to get started.

# Dependencies to be Installed
* Python Twitter Tools
* json / simplejson 

# Other Requirements
You'll need a twitter developer account, so that you can grab the 
* ACCESS_KEY
* ACCESS_SECRET
* CONSUMER_KEY
* CONSUMER_SECRET

to run the script.

# How to run the file?
##### Type the following in the command terminal:
$ python twitter_streaming.py > twitter_stream_1000tweets.txt
##### This will create a new twitter_stream_1000tweets.txt file in the working directory. Now run the printData.py script.
$ python printData.py
