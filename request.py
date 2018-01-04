import requests
import json

DATA = {
	'jsonrpc': "2.0",
	'method': "generateIntegers",
	'params': {
		'apiKey': "00000000-0000-0000-0000-000000000000",
		'n': 16384,
		'min': 0,
		'max': 1,
		'replacement': true,
	},
	'id': 0
}
def make_request(url="https://api.random.org/json-rpc/1/invoke"):
	request = requests.get(url, data=json.dumps(DATA), headers=HEADERS)
	return request.text

#make_request()