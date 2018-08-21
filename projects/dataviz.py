import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitterdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []

for tweet in tweetData:
    print("Tweet text: ", tweet['text'])

file = open("twitterdata.json", "r")
olddata = json.load(file)
list.extend(polarity)
file.close()

listToJSON = json.dumps(list)
file = open("twitterdata.json", "w")
file.write(listToJSON)
file.close()

def findAveragePolarity(data):
    sum = 0
    for entry in data:
        sum += int(entry['age'])
    return sum / len(data)

def main():
    file = open("twitterdata.json", "r")
    data = json.load(file)
    print("Analyzing data...")
    averagePolarity = findAveragePolarity(data)
    print("Average polarity: %d" %averagePolarity)

if __name__ == "__main__":
    main()
# Textblob sample:
#tb = TextBlob("You are a very magnificent and computer scientist.")
print(tb.polarity)
