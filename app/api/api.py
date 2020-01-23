##########################
# Python 3.x Example
##########################

# package used to execute HTTP POST request to the API
import json
import urllib.request

# API Key
TOKEN = "e4c499a78ef71b7f2457cdef80f9a1f8df374af6d71dc787f7e3f2e1671cfca7" # replace YOUR_API_KEY with the API key you got from sec-api.io after sign up
# API endpoint
API = "https://api.sec-api.io?token=" + TOKEN

# define the filter parameters you want to send to the API 
payload = {
  "query": { "query_string": { "query": "filedAt:{2020-01-16} AND formType:\"NPORT-P\"" } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

# format your payload to JSON bytes
jsondata = json.dumps(payload)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes

# instantiate the request 
req = urllib.request.Request(API)

# set the correct HTTP header: Content-Type = application/json
req.add_header('Content-Type', 'application/json; charset=utf-8')
# set the correct length of your request
req.add_header('Content-Length', len(jsondataasbytes))

# send the request to the API
response = urllib.request.urlopen(req, jsondataasbytes)

# read the response 
res_body = response.read()
# transform the response into JSON
filings = json.loads(res_body.decode("utf-8"))

# print JSON 
print(filings)