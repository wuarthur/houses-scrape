import requests
from headers import header, data
import json
from pprint import pprint

response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=header, data=data)

with open('test.json', 'w') as fout:
    fout.write(response.text)


j = json.loads(response.text)
pprint(j)