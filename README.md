# metacritic_scraper

A web-scraping project which aims to scrape game score data from [metacritic.com](https://www.metacritic.com/), perform ETL and show some statistics about game scores.

![](ms_logo.png)

For this project, the goal is to collect data on [upcoming & recently released PS4 games](https://www.metacritic.com/browse/games/release-date/available/ps4/date). 


This project can be divided into 3 sections. 
1. webscraping the website using  Python3 & BeautifulSoup 
2. cleaning and transforming the data using Pandas
3. sending an email (Gmail) with some statistics derived from the data / save data as csv

<br>SAMPLE EMAIL CAN BE FOUND IN **sample_email.txt**

<br>

## Instructions for Users
---

### 1. Set up the environment

First, install required packages or create a virtual enviroment using conda and ```environ.yaml``` file

```
$ conda env create -f environ.yaml 
```
Then you can just run the code below to activate the environment
```
$ conda activate meta-scraper
```
Here are the required packages
```
  - beautifulsoup4
  - numpy
  - pandas
```
<br>

### 2. Set up the environment variables
To send an email using Gmail, we need to set up:
- **GMAIL**: email to send emails from
- **GMAILPASS**: password for the gmail accout

```email_data.py``` script uses environment variables "GMAIL" and "GMAILPASS".
Here is a [guide](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) to set those variables on your machine.

Or alternatively, you can **hardcode** your gmail and password directly in the ```email_data.py``` script. 

<br>

### 3. Run the script!

Once everything is all set, run ```scraper.py``` script and you should be prompted to enter the destination email address :
```
Please enter the email address to send this email to: 
```

Now check your gmail you specified when setting up the environment variable GMAIL, and you should find the email sent by the script. 

Also you should be able to find a csv file with the same data in out_csv_file folder. 





## Breakdown of the Project
---

//ETL description

**Send Email with Some Game Score Insights & Statistics**

// attach example email



