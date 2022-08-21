import requests as req
import pprint


try:
    result = req.get('https://api.ipify.org?format=json')

    pprint.pprint(result.json())
except:
    pprint.pprint('couldnt fetch api ')