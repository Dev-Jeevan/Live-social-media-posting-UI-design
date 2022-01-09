import praw
import requests
import pandas as pd
from datetime import datetime
import pymongo
import certifi
from praw import reddit
import json

Client_ID = 'HHPY0Bl6K9J9bS1CXcGQdQ'
Secret_key = 'NwrD-7embfoNBIst3FCRpCY2M57Csg'

auth = requests.auth.HTTPBasicAuth(Client_ID, Secret_key)

data = {
    'grant_type' : 'password',
    'username':'ShanJeevan94',
    'password':'aksheka07',
}

reddit = praw.Reddit(client_id = 'HHPY0Bl6K9J9bS1CXcGQdQ',
                         client_secret = 'NwrD-7embfoNBIst3FCRpCY2M57Csg',
                         username = 'ShanJeevan94',
                         password = 'aksheka07',
                         user_agent = 'Jeevan')

RedditUsername = "ShanJeevan94"

df = pd.DataFrame()

def new_reddit(heading,body):
    subr = 'pythonsandlot'  # Choose your subreddit
    subreddit = reddit.subreddit(subr)  # Initialize the subreddit to a variable
    title = heading
    selftext = body
    subreddit.submit(title, selftext=selftext)
    return  None

Posts = []
for post in reddit.redditor(RedditUsername).submissions.top():
        df = df.append({"ID":post.id,
                     "Title":post.title,
                     "Description":post.selftext,
                     "Score":post.score,
                     "Timestamp":datetime.fromtimestamp(post.created)}, ignore_index=True)

print (df)


ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Jeevan:aksheka07@cluster0.vqsfw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

db = client["Web_Scraping"]
collection = db["Reddit"]
collection.insert_many(df.to_dict('records'))