import requests
from bs4 import BeautifulSoup
from csv import writer,reader
import crawl_database

url = "https://www.rithmschool.com"
response = requests.get(url)
with open("crawled_database.csv", "a") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow([url])
soup = BeautifulSoup(response.text, 'html.parser')
original_links = soup.find_all('a')
length_of_database = len(original_links)
for i in range(length_of_database):
    links = soup.find_all('a')[i]['href']
    if "/" in links:
        if 'com' not in links:
            source_links = url + links
            with open("original_databse.csv", "a") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow([source_links])



crawl_database.crawling_database()
