import requests
from bs4 import BeautifulSoup
from csv import writer, reader


def crawling_database():
    link_list = []
    clink_list = []
    ck_list = set()
    with open("original_databse.csv") as file:
        csv_reader = reader(file)

        for fighter in csv_reader:
            link_list.append(fighter)
        for i in range(len(link_list)):
            if len(link_list[i]) > 0:
                url = link_list[i][0]

                with open("crawled_database.csv") as lfile:
                    csv_reader = reader(lfile)
                    for fighter in csv_reader:
                        clink_list.append(fighter)
                    for j in range(len(clink_list)):
                        if len(clink_list[j]) > 0:
                            curl = clink_list[j][0]
                            ck_list.add(curl)
                if url not in ck_list:
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
                                source_links = url + links[1:]
                                print(source_links)
                                with open("original_databse.csv", "a") as csv_file:
                                    csv_writer = writer(csv_file)
                                    csv_writer.writerow([source_links])

