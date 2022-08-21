import requests
from pprint import pprint
try:
    url = "https://genius.p.rapidapi.com/artists/16775"

    headers = {
        "X-RapidAPI-Key": "c7ccb727bemsh820f82fd14a46dbp1bb1e7jsn2847a6613051",
        "X-RapidAPI-Host": "genius.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    pprint(response.text)

    for i in response:
        pprint(i)
except:
    print('Request returned error')







data = response.json()


request = response.request
print(request.url)