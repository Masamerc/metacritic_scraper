import requests
from bs4 import BeautifulSoup
import json
from data_wrangler import DataHelper
from email_data import send_email
import datetime 

url = 'https://www.metacritic.com/browse/games/release-date/available/ps4/date'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

games = soup.find_all("div", {"class":"product_wrap"})[:-3]

# scrape the name, release date, user score and critic score of each game and store them in a dictionary
game_data = []
for game in games:
     title = game.find("div", {"class":"basic_stat product_title"})

     for tag in game.find_all("li", {"class":"stat release_date"}):
          release_date = tag.find("span", {"class":"data"})
     
     critic_score = game.find_all("div", {"class":"basic_stat product_score brief_metascore"})[0]
     user_score = game.find_all("span")[1]
     pair = {
          "title":title.text.strip(),
          "release_date":release_date.text.strip(),
          "critic_score":critic_score.text.strip(),
          "user_score":user_score.text.strip()
     }
     game_data.append(pair)

# save the dictionary as JSON so the DataHelper can receive and convert it into dataframe
with open("data.json", "w") as f:
     json.dump(game_data, f, indent=2)

# create an instance of DataHelper 
dh = DataHelper

# perform operations of DataHelper 
test_data = dh.load_and_clean()
complete_data = dh.get_complete_data(test_data, save_csv=True)
o_best = dh.store_overall_best(complete_data)
u_best = dh.store_users_best(complete_data)
c_best = dh.store_critic_best(complete_data)
contr_good = dh.store_controverial_good(complete_data)
contr_bad = dh.store_controverial_bad(complete_data)



# prompt the user to put email address to send email to
to_address = input("Please type the email address that recieves this email: ")

send_email(subject=f"Metacritic Scraper {datetime.date.today()}", content=o_best + "\n" + u_best\
          + "\n" + c_best + "\n" + contr_good + "\n" + contr_bad, to_address=to_address)