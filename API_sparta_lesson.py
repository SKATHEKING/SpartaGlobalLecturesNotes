import requests as req
import pprint

result = req.get('https://api.chucknorris.io/jokes/random')

pprint.pprint(result.json()['value'])


