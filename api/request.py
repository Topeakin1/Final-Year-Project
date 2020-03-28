
import requests
import json

url = 'http://127.0.0.1:5000/'

data = 'Mike lowry does not die in BAD BOYS'
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
