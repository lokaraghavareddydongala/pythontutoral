from pymongo.mongo_client import MongoClient
import urllib

uri = "mongodb+srv://lokaraghavareddy:" + urllib.parse.quote(
    "Raghav@1") + "@cluster0.l6wez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.test
print(db)

d = {"name": "raghava",
     "email": "lokaraghavareddy@gmail.com",
     "surname": "dongala"
     }
db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)
