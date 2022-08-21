import pymongo

client = pymongo.MongoClient()

db = client['starwars']

luke = db.characters.find_one({'name':'Luke Skywalker'})

droids = db.characters.find({'species':'Droid'})
for droid in droids:
    print(droid['name'])

darth_vader_stats = db.characters.find({'name':'Darth Vader'}, {'name': 1 , 'height': 1})

yellow_eyes_characters = db.characters.find({'eye_color': 'yellow'}, {'name' : 1 })

male_characters = db.characters.find({'gender' : 'male'},{'name':1}).limit(3)

alderanians = db.characters.find ({'species.name':'Human', 'homerworld.name':'Alderaan'})