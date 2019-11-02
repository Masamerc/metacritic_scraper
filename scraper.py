import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.metacritic.com/browse/games/release-date/available/ps4/date'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

games = soup.find_all("div", {"class":"product_wrap"})[:-3]


game_data = []
for game in games:
     title = game.find("div", {"class":"basic_stat product_title"})
     for tag in game.find_all("li", {"class":"stat release_date"}):
          release_date = tag.find("span", {"class":"data"})

     pair = {
          "title":title.text.strip(),
          "release_date":release_date.text.strip()
     }
     game_data.append(pair)

# for title in titles:
#     print(title.text)

with open("data.json", "w") as f:
     json.dump(game_data, f, indent=2)
