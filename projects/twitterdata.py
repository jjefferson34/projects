import json

tweetFile = open("twitterdata.json", "r")
tweetData = json.load(tweetFile)

print(tweetData)
