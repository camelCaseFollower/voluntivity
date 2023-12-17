import classes
import pymongo

# Replace the placeholder with your Atlas connection string
uri = "<connection string>"
# Set the Stable API version when creating a new client
client = pymongo.MongoClient(uri, server_api=pymongo.ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

print("enter your name:",end =" ")
name = input()

print("enter your age:",end =" ")
age = int(input())

print("enter your country:",end =" ")
country = input()

h1 = classes.human(name,age,country)
print(h1)