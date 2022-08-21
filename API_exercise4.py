import requests as req
import pprint

try:
    result = req.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    pprint.pprint(result.json())
except:
    pprint('COULDNT FETCH API')
