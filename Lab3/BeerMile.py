import requests
from bs4 import BeautifulSoup
from Record import Record
import re
import threading
from threading import Thread

sem = threading.Semaphore(2)


class BeerMile(Thread):
    def __init__(self, email, password):
        Thread.__init__(self)
        self.username = email
        self.password = password
        self.login_url = 'https://www.beermile.com/?action=login'
        self.top_1000 = 'https://www.beermile.com/records/ref_wr'
        self.main_page = 'https://www.beermile.com/'
        self.content = ''
        self.records = []
        self.time_best_alco_runner = ''
        self.sec_best_alco_runner = 0.0
        self.rec1 = []  # 2 - 250
        self.rec2 = []  # 251 - 500
        self.rec3 = []  # 501 - 750
        self.rec4 = []  # 751 - 1000
        self.curSession = requests.Session()

    def login(self):
        values = {'username': self.username,
                  'password': self.password
                  }
        request_post = requests.post(self.login_url, data=values)
        print(request_post)
        bingo = (request_post.text).find("Logout")
        print(bingo)

    def getLoginCookies(self):
        login_url = 'https://www.beermile.com/?action=login'
        values = {'username': self.username,
                  'password': self.password
                  }
        #  all cookies received will be stored in the session object
        self.curSession.post(self.login_url, data=values)
        # internally return your expected cookies, can use for following auth
        self.getPageCookies()

    def getPageCookies(self):
        # internally use previously generated cookies, can access the resources
        request_get = self.curSession.get(self.main_page)
        self.content = request_get.text
        print(request_get)
        bingo = (request_get.text).find("Logout")
        print(bingo)

    def getPage(self):
        request_get = requests.get(self.main_page)
        self.content = request_get.text
        bingo = (request_get.text).find("Logout")
        print(bingo)
        # print(self.content)

    def getPageTop1000(self):
        request_get = requests.get(self.top_1000)
        self.content = request_get.text
        # print(self.content)

    def getTop1000(self):
        self.getPageTop1000()
        soup = BeautifulSoup(self.content, 'lxml')
        table_html = soup.find_all('table')[0]
        # print(table_html)

        # Parse table
        nr = 0
        for table_row in table_html.findAll("tr"):
            # Find Name
            name = re.search("\>([a-zA-Z0-9\"\.\s]+)\<", str(table_row.findAll("td", class_="records_name")))
            if name:
                name = name.group(1)
            # Find Time
            time = re.search("\>([\s]*[0-9]+[\:]+[0-9]+[\.]*[0-9]*[\s]*)\<",
                             str(table_row.findAll("td", class_="records_time")))
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
            beer = re.search("beertype_[a-zA-Z\"\+\s]+\>([a-zA-Z\s]+)\<\/a\>\<\/td\>",
                             str(table_row.findAll("td", nowrap="")))
            if beer:
                beer = beer.group(1)
            self.records.append(Record(nr, name, time, year, beer))
            nr += 1

        self.records[0] = Record("Nr.", "Name", "Time", "Year", "Beer")
        rec_best = self.records[1]
        self.time_best_alco_runner = rec_best.records_time
        # print(self.time_best_alco_runner)
        self.timeToSec()
        rec_best = self.records[1]
        self.sec_best_alco_runner = rec_best.records_time
        # print(self.sec_best_alco_runner)
        self.divideList()
        self.startThreads()

    def timeToSec(self):
        for rec in self.records:
            if rec.records_time != "Time":
                split_time = rec.records_time.split(":")
                min = 0.0
                sec = 0.0
                n = 0
                for t in split_time:
                    if n == 0:
                        min = t
                    if n == 1:
                        sec = t
                    n += 1
                sec_tot = float(sec) + (float(min) * 60)
                rec.records_time = sec_tot

    def divideList(self):
        for i in range(2, 251):
            self.rec1.append(self.records[i])
        for i in range(251, 501):
            self.rec2.append(self.records[i])
        for i in range(501, 751):
            self.rec3.append(self.records[i])
        for i in range(751, 1001):
            self.rec4.append(self.records[i])

    def getTimeDiff(self, rows):
        sem.acquire()
        for rec in rows:
            diff_sec = rec.records_time - self.sec_best_alco_runner
            min = int(diff_sec) // 60
            sec = round((float(diff_sec) % 60), 2)
            rec.records_time = "+" + str(min) + ":" + str(sec)
        print(threading.current_thread())
        sem.release()

    def startThreads(self):
        threads_list = []
        t1 = Thread(target=self.getTimeDiff, args=([self.rec1]))
        t2 = Thread(target=self.getTimeDiff, args=([self.rec2]))
        t3 = Thread(target=self.getTimeDiff, args=([self.rec3]))
        t4 = Thread(target=self.getTimeDiff, args=([self.rec4]))

        threads_list.append(t1)
        threads_list.append(t2)
        threads_list.append(t3)
        threads_list.append(t4)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        for thread in threads_list:
            thread.join()

        rec = self.records
        best_alco_runner = rec[1]
        best_alco_runner.records_time = self.time_best_alco_runner
        self.displayTable()

    def displayTable(self):
        for rec in self.records:
            print(format(str(rec.record_position), ' ^3s'),
                  " | ", format(str(rec.records_name), ' ^25s'),
                  " | ", format(str(rec.records_time), ' ^9s'),
                  " | ", format(str(rec.records_year), ' ^5s'),
                  " | ", format(str(rec.records_beer), ' ^20s'), "\n")
