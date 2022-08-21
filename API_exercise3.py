import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games/borderlands"

headers = {
	"X-RapidAPI-Key": "c7ccb727bemsh820f82fd14a46dbp1bb1e7jsn2847a6613051",
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)