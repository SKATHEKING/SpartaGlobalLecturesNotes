import pymongo

client = pymongo.MongoClient('mongodb://52.28.118.187:27017')
db = client['DummyDatabase']

db.create_collection('Towns')