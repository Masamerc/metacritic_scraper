# metacritic_scraper

A web-scraping project which aims to scrape game score data from [metacritic.com](https://www.metacritic.com/), perform ETL and show some statistics about game scores.

![](/assets/ms_logo.png)

For this project, the goal is to collect data on [upcoming & recently released PS4 games](https://www.metacritic.com/browse/games/release-date/available/ps4/date). 

You can use docker to run the program as well. [Run with Docker](#Run-with-Docker🐋)


This project can be divided into 3 sections. 
1. webscraping the website using  Python3 & BeautifulSoup 
2. cleaning and transforming the data using Pandas
3. sending an email (Gmail) with some statistics derived from the data / save data as csv

<br>*SAMPLE EMAIL CAN BE FOUND HERE [HERE](assets/sample_email.txt)

<br>

## Instructions for Users
---

### 1. Set up the environment

First, install required packages or create a virtual enviroment or install these packages with requirements.txt file.
```
pip install -r requirements.txt
```
<br>

### 2. Set up the environment variables
To send an email using Gmail, you need to either:
- Create a new Gmail account and allow "Less Secure Apps" in settings
- Or allow "Less Secure Apps" in settings for your existing Gmail account

[Here](https://hotter.io/docs/email-accounts/secure-app-gmail/)'s a guide for doing so. 

<br>

### 3. Run the script!

Once everything is all set, run ```scraper.py``` script and you should be prompted to enter the destination email address :
```
Please enter the email address to send this email to: 
```

Now check your gmail specified for destination, and you should find the email sent by the script. 

Also you should be able to find a csv file with the scraped data in out_csv_file folder. 


<br>


## Breakdown of the Project
---

## 1. Data Extraction (```scraper.py```)
As detailed in the top of this documentation, the extracted data is taken from  metacritic.com. The script utilizes the beautifulsoup4 library to target and extract the specific HTML elements on the page: 
- title
- release date
- user score
- critic score

and the script stores them in JSON file which will be passed on to ```data_wrangler.py``` script, which cleans and transforms the data into some meaningful information returned as strings.
Those strings will be then injected into ```send_email``` fucntion imported from ```email_data.py``` and will be sent to specified email address.

##  2. Data Cleaning and Transformation (```data_wrangler.py```)

Data wrangling process is done within ```data_wrangler.py``` script, which has a class **DataHelper** with following static/utility methods:
- load_and_clean(): loads the scraped JSON data and returns cleaned dataframe

- get_complete_data(): performs a serires of data cleaning & feaure engineering then returns the complete data as pandas dataframe. if argument save_csv == True, data will be saved as a csv file in out_csv_files directory.

- store_overall_best(): returns top 5 overall best videogames with details

- store_critic_best(): returns top 5 best videogames with details reviewed by critics

- store_user_best(): returns top 5 best videogames reviewed by users

- store_controverial_good(): returns top 5 most controversial games with the biggest 
positive gaps between critic score and user score

- store_controverial_bad(): returns top 5 most controversial games with the biggest 
negative gaps between critic score and user score
## 3. Loading Data and Sending Email (```email_data.py```)
The main script ```scraper.py``` sends an email to a specified email address, and also saves data in a csv file. 

```email_data.py``` script is in charge of sending an email, and for that it uses smtplib. Please be advised that **it only works with GMAIL** 

<br>

---

### Run with Docker🐋

1. Build a docker container with the supplied Dockerfile. You can name the container whatever you want. 

```docker
# Dockerfile

FROM python:3.7-slim

COPY . /user/src/app
WORKDIR /user/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD python scraper.py
```
```
$ docker build . -t CONTAINER_NAME
```

2. Run the container like so: (make sure you use the "-it" tag since it you have to type in some credentials interactively during the execution of script)
```
$ docker run -it CONTAINER_NAME
```


