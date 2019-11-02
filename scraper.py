import requests
from bs4 import BeautifulSoup

url = 'https://www.metacritic.com/browse/games/release-date/available/ps4/date'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

games = soup.find_all("div", {"class":"product_wrap"})[:-3]

# titles = soup.find_all("div", {"class":"basic_stat product_title"})
# titles = soup.select("div.basic_stat.product_title > a")

# for title in titles:
#     print(title.text)

print(games[-1])