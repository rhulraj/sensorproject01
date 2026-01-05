from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url = "mongodb+srv://rahulraj:software.mdb@cluster0.mwjyvs2.mongodb.net/?appName=Cluster0"

#create a new client and connect to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME = 'rahulraj'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv('D:\Users\rahul\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv')

df = df.drop('Unnamed: 0', axis =1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

