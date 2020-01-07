######################################################
# 
# Libraries
#
######################################################

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
import requests
from bs4 import BeautifulSoup
import json


######################################################
# 
# App instance
#
######################################################

app = Flask(__name__)


######################################################
# 
# Routes
#
######################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape')
def scrape():
    #flash(request.args.get('url'), 'success')
    url = request.args.get('url')
    
    try:    
        response = requests.get(url)
        content = BeautifulSoup(response.text, 'lxml').prettify()
    except:
        flash('Failed to retrieve URL "%s"' % url, 'danger')
        content = ''

    return render_template('scrape.html', content=content)

# render results to screen
@app.route('/results')
def results():



    urlnostrip = request.args.get('url')

    url = urlnotrip.strip()

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'xml')

    fundName = soup.find("seriesName")
    fundNameString = fundName.text.replace('.','').replace("/","")

    totAssets = soup.find("totAssets").text

    reportDate = soup.find("repPdDate")
    reportDateString = str(reportDate.text)

    regCIK = soup.find("regCik").text

    onlySecs = soup.findAll("invstOrSec")

    counter = 0

    header = "Issue name, ISIN, Share, Value, Long-Short, Asset category, Total assets:," + str(totAssets)

    results = []

    for i in onlySecs:


        issueNamesTextFirst = onlySecs[counter].title.text
        issueNamesText = str(issueNamesTextFirst).replace("\n","").replace(",","")

        isinTextFirst = onlySecs[counter].isin
        isinTextStringer = str(isinTextFirst)
        isinText = isinTextStringer.replace('<isin value="','').replace('"/>','')

        if isinText == None:
            isinText = ""

        sharenumberTextFirst = onlySecs[counter].balance.text
        shareNumberText = str(sharenumberTextFirst).replace("\n","")   

        if shareNumberText == None:
            shareNumberText = ""

        valueUSDTextFirst = onlySecs[counter].valUSD.text
        valueUSDText = str(valueUSDTextFirst).replace("\n","")

        if valueUSDText == None:
            valueUSDText = ""

        payoffProfileTextFirst = onlySecs[counter].payoffProfile.text
        payoffProfileText = str(payoffProfileTextFirst).replace("\n","")

        if payoffProfileText == None:
            payoffProfileText = ""

        if onlySecs[counter].assetCat == None:
            assetCategoryText = onlySecs[counter].assetConditional["desc"]
        else:
            assetCategoryTextFirst = onlySecs[counter].assetCat.text
            assetCategoryText = str(assetCategoryTextFirst).replace("\n","")

        if assetCategoryText == 'EC':
            assetCategoryText = 'Equity-common'

        if assetCategoryText == 'DBT':
            assetCategoryText = 'Debt'

        if assetCategoryText == 'STIV':
            assetCategoryText = 'Short-term investment vehicle'

        if assetCategoryText == 'ABS-MBS':
            assetCategoryText = 'ABS-mortgage backed security'

        if assetCategoryText == 'ABS-O':
            assetCategoryText = 'ABS-other'

        if assetCategoryText == 'ABS-CDBO':
            assetCategoryText = 'ABS-collateralized bond-debt obligation'

        if assetCategoryText == 'SN':
            assetCategoryText = 'Structured note'

        if assetCategoryText == 'LON':
            assetCategoryText = 'Loan'

        if assetCategoryText == 'EP':
            assetCategoryText = 'Equity-preferred'

        if assetCategoryText == 'DFE':
            assetCategoryText = 'Derivative-foreign exchange'

        if assetCategoryText == 'DIR':
            assetCategoryText = 'Derivative-interest rate'

        if assetCategoryText == 'DE':
            assetCategoryText = 'Derivative-equity'

        if assetCategoryText == None:
            assetCategoryText = ""


        """
        issuerCategoryTextFirst = issuerCategory[counter]
        issuerCategoryText = issuerCategoryTextFirst.text

        if issuerCategoryText == 'CORP':
            issuerCategoryText = 'Corporate'

        if issuerCategoryText == 'MUN':
            issuerCategoryText = 'Municipal'

        if issuerCategoryText == 'RF':
            issuerCategoryText = 'Registered fund'

        if issuerCategoryText == 'USGSE':
            issuerCategoryText = 'U.S. government sponsored entity'

        if issuerCategoryText == 'USGA':
            issuerCategoryText = 'U.S. government agency'

        if issuerCategoryText == 'UST':
            issuerCategoryText = 'U.S. Treasury'

        """

        args = []
        
        
        row = (str(issueNamesText) + "," + isinText + "," + shareNumberText + "," + valueUSDText + "," + payoffProfileText + "," + assetCategoryText).split(",")

        results.append(row)

        counter = counter + 1
    
    return render_template('results.html', results=results, fundNameString=fundNameString, reportDateString=reportDateString, regCIK=regCIK, totAssets=totAssets)


######################################################
# 
# Run app
#
######################################################

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True, threaded=True)
