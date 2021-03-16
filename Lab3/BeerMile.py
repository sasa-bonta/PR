import requests
from bs4 import BeautifulSoup
from Record import Record
import re

class BeerMile:
    def __init__(self, email, password):
        self.username = email
        self.password = password
        self.login_url = 'https://www.beermile.com/?action=login'
        self.top_1000 = 'https://www.beermile.com/records/ref_wr'
        self.content = ''

    def login(self):
        values = {'username': self.username,
                  'password': self.password
                  }
        request_post = requests.post(self.login_url, data=values)
        print(request_post)

    def getPage(self):
        request_get = requests.get(self.top_1000)
        self.content = request_get.text
        # print(self.content)

    def getTop1000(self):
        soup = BeautifulSoup(self.content, 'lxml')
        table_html = soup.find_all('table')[0]
        # print(table_html)

        # Parse table
        records = []

        nr = 0
        for table_row in table_html.findAll("tr"):
            # Find Name
            name = re.search("\>([a-zA-Z0-9\"\.\s]+)\<", str(table_row.findAll("td", class_="records_name")))
            if name:
                name = name.group(1)
            # Find Time
            time = re.search("\>([\s]*[0-9]+[\:]+[0-9]+[\.]*[0-9]*[\s]*)\<", str(table_row.findAll("td", class_="records_time")))
            if time:
                time = time.group(1)
                time = re.sub(r"[\n\t\s]*", "", time)
            # Find Year
            year = re.search("\>([\s]*[0-9]{4}[\s]*)\<", str(table_row.findAll("td", class_="records_year")))
            if year:
                year = year.group(1)
                year = re.sub(r"[\n\t\s]*", "", year)
            # Find Beer
            # beer = table_row.findAll("td", nowrap="")
            beer = re.search("beertype_[a-zA-Z\"\+\s]+\>([a-zA-Z\s]+)\<\/a\>\<\/td\>", str(table_row.findAll("td", nowrap="")))
            if beer:
                beer = beer.group(1)
            records.append(Record(nr, name, time, year, beer))
            nr += 1

        records[0] = Record("Nr. | ", "Name | ", "Time | ", "Year | ", "Beer")

        for rec in records:
            print(rec.record_position)
            print(rec.records_name)
            print(rec.records_time)
            print(rec.records_year)
            print(rec.records_beer)
            print("\n")

            # lalalalal