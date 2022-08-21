import requests
from pprint import pprint

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
	"X-RapidAPI-Key": "c7ccb727bemsh820f82fd14a46dbp1bb1e7jsn2847a6613051",
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
pprint(response.json())
pprint(response.text[int(len(response.text)/2):-1])
