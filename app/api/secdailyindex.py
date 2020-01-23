from urllib.request import urlopen

fileDate = input("Please input the date in YYYYMMDD format (e.g. 20200122) : ")

base_url = "https://www.sec.gov/Archives/edgar/daily-index/"
dailyfilings = []

yearUrl = fileDate[:4]
monthUrl = fileDate[4:-2]

if 1 <= int(monthUrl) <= 3:
    QTR = "QTR1"

if 4 <= int(monthUrl) <= 6:
    QTR = "QTR2"

if 7 <= int(monthUrl) <= 9:
    QTR = "QTR3"

if 10 <= int(monthUrl) <= 12:
    QTR = "QTR4"

lines = urlopen(str(base_url) + str(yearUrl) + "/" + str(QTR) + "/" + "crawler." + fileDate + ".idx").read().decode('ascii').split("\n")

for line in lines:
    if "NPORT-P" in line:
        dailyfilings.append(line)

if dailyfilings == []:
    dailyfilings.append("No such filling for NPORT-P for: " + str(fileDate))

print("\n".join(dailyfilings))