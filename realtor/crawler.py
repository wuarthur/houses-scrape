import requests
from headers import header, data
import json
from pprint import pprint


def get_page(page):
    r"""get a page of json data form realtor.com.
    :param page: the page you want to request.
    :return: Json Object
    :return: Int (Status_code, 400 indicates page out of range)
    """
    page = str(page)
    data['CurrentPage']=page
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=header, data=data)
    JSON =  json.loads(response.text)
    status_code=JSON['ErrorCode']['Id']
    if status_code == 400:
        print( "WARNING: page number %s out of range" % page)
    return JSON, status_code

####usage
# Json, status_code = get_page(400)
# pprint(Json)