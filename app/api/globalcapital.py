import requests
from bs4 import BeautifulSoup

url = input("Please input the url to be scraped from globalcapital archive: ")

#url = "https://www.globalcapital.com/archive/2020/01"
base_url = "https://www.globalcapital.com"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

articles = soup.find('ul', {"class":"article-list archive"})

articleList = articles.findAll("li")

counter = 0

filename = "globalcapital.csv"
f = open(filename, "a", encoding="utf-8")
headers = "Title, Summary, Date, Link, \n"

f.write(headers)

for article in articleList:
    articleTitle = articleList[counter].h2.text.replace(",","")
    articleSummary = articleList[counter].p.text.replace(",","")
    articleLink = articleList[counter].a['href']
    fullArticleLink = base_url + articleLink
    articleDate = articleList[counter].find('p', {"class":"small-text right"}).text.replace(",","")

    print(articleTitle)
    print(articleSummary)
    print(fullArticleLink)
    print(articleDate)
    print("")

    f.write(articleTitle + "," + articleSummary + "," + articleDate + "," + fullArticleLink + "\n")

    counter = counter + 1