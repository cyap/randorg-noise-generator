import requests
import json

URL = "https://api.random.org/json-rpc/1/invoke"
HEADERS = {'User-Agent' : "cyap@slu.edu"}

def make_randorg_request(method, params, url=URL):
	data = {
		'jsonrpc': "2.0",
		'method': method,
		'params': params,
		'id': 0
	}
	request = requests.get(url, data=json.dumps(data), headers=HEADERS)
	return json.loads(request.text)