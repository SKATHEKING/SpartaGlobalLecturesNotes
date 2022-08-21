import json

import jsonfile as jsonfile

dic_to_upload = {'name': 'data','status':1}

with open('data.json','w'):
    json.dump(dict, jsonfile)