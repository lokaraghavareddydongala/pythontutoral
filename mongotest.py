from pymongo.mongo_client import MongoClient
import urllib

# Mongo Db Atlas cloud
uri = "mongodb+srv://lokaraghavareddy:" + urllib.parse.quote(
    "Raghav@1") + "@cluster0.l6wez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.test
print(db)

d2 = {"_id": 2,
      "name": "reddy1",
      "email": "lokaraghavareddy@outlook.com",
      "hobbies": ["reading", "playing"],
      "StatusMarried": True
      }

# list of documents
d3 = [{"name": "reddy3", "email": "lokaraghavareddy@outlook3.com"},
      {"name": "reddy4", "email": "lokaraghavareddy@outlook4.com"}
      ]
# creating the database
database = client['mongotest']
# creating the collection
# col1 = db1['test']
collection = database['test2']

# Adding the single document
# collection.insert_one(d2)

# Adding the many documents
# collection.insert_many(d3)

# Displaying all documents in the collection
# records = collection.find()
#
# for i in records:
#       print(i)


# query where name is reddy1
# records = collection.find({"name":"reddy1"})
# for i in records:
#       print(i)

records = collection.find()
for i in records:
      print(i)

