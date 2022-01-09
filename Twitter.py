import sys
import tweepy
import pandas as pd
import pymongo
import certifi
from pymongo import MongoClient

# Authenticate to Twitter

CONSUMER_KEY = 'cwwubaTYZZa4YSFuLHNTCtfFa'
CONSUMER_SECRET = 'oppQyDXflPpGjXB4k7Xa9SDsniNRgGoq1w2KuxbuIwujKK8pnE'
ACCESS_TOKEN = '1443681565888876555-W9Z6kQuAbKXYfz6c2VP5MzAMv1nw8b'
ACCESS_TOKEN_SECRET = 'WWjcRwHOZlfxg2Kr8bhk4GXVGZBrKay7p8qlaIR1ehn0z'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


filename = "tweet.csv"
f = open(filename, "w")
headers = "User Name,Tweet\n"
f.write(headers)

"""
def get_tweet(input):
    api.update_status(input)
    return None


get_tweet("mfdfds")
"""
#post new tweeet
def get_tweet():
    #api.update_status('Hi there ssssddvfg')
    new_tweet = input("Enter new tweet:")
    api.update_status(new_tweet)
    return None
get_tweet()

timeline = api.home_timeline()

for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

    f.write(tweet.user.name + "," + tweet.text + "\n")

f.close()


# Import CSV Files into Pandas Dataframes

df = pd.read_csv("tweet.csv")
print(df)

# connecting to mongo DB and storing the data
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://Jeevan:aksheka07@cluster0.vqsfw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

db = client["Web_Scraping"]
collection = db["Twitter"]

collection.insert_many(df.to_dict('records'))
#collection.insert_one({"_id": 0, "Twitter_name": "Jeeva"})



""""
def OAuth():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

    except Exception as e:
        return print('error')

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('New Tweet 000001')
print('new post')

"""