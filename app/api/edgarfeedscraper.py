import requests
from bs4 import BeautifulSoup
import time

#url = input("Please input the url to be scraped from globalcapital archive: ")

url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=NPORT-P&company=&dateb=&owner=include&start=0&count=100&output=atom"
IDlist = []

entrycounter = 0

filename = "NPORT_P.csv"
f = open(filename, "a", encoding="utf-8")
headers = "EDGAR name, Filing Date, Link, ID" + "\n"

f.write(headers)

while True:
  
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    entries = soup.findAll("entry")

    print("")
    print(len(entries))
    print("")

    if entries != None:

        for entry in entries:

            if entry.id.text not in IDlist:

                f = open(filename, "a", encoding="utf-8")

                filingName = entry.title.text.replace("NPORT-P - ","")
                documentLink = entry.link["href"]
                updateDate = entry.updated.text
                ID = entry.id.text
                IDnoComma = ID.replace(",","")
                IDlist.append(ID)

                print("NEW ENTRY!")
                print("")
                print(filingName)
                print(documentLink)
                print(updateDate)
                print(ID)
                print("")
                print(IDlist)
                print(len(IDlist))
                print("")

                if len(IDlist) > 128:
                    IDlist = []

                f.write(filingName + "," + updateDate + "," + documentLink + "," + IDnoComma + "\n")
                f.close()

                entrycounter = entrycounter + 1

            else:
                
                print("")
                print("No new entry")
                print("")

    time.sleep(60) 