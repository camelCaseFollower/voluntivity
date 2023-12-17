from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://voluntivity_admin:!root4win@allin.gln3k5z.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

#connect to database and create a new collection
database = client["allin"]
accounts = database["accounts"]

new_user = {
    "username":username,
    "password":password,
}

accounts.insert_one(new_user) #onclick

client.admin.command('ping')
