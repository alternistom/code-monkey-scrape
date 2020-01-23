import requests
from bs4 import BeautifulSoup
import time

#url = input("Please input the url to be scraped from globalcapital archive: ")

url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=NPORT-P&company=&dateb=&owner=include&start=0&count=40&output=atom"
ID = ""

while True:
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    entries = soup.findAll("entry")
    firstEntry = entries[0]

    if firstEntry.id.text != ID:

        filingName = firstEntry.title.text.replace("NPORT-P - ","")
        documentLink = firstEntry.link["href"]
        updateDate = firstEntry.updated.text
        ID = firstEntry.id.text

        print("NEW ENTRY!")
        print("")
        print(filingName)
        print(documentLink)
        print(updateDate)
        print(ID)
        print("")

    else:
        print("")
        print("No new entry")
        print("")

    time.sleep(1)