""" SNS Requests
"""

import json
from requests import post, get

BASE_URL = "http://127.0.0.1:5000"
#BASE_URL = "http://ec2-54-175-80-131.compute-1.amazonaws.com"

# data = '{"id":"dfjdkf734dsc87","first_name":"sns_api1","last_name":"Stevenson","telephone_number":"07777456278","email_address":"test@holmescentral.co.uk"}'
# data3 = {"id":"reh56fjr743478","first_name":"sns_api3","email_address":"test@holmescentral.co.uk"}
# data4 = "{'id':'rehekjr743478','first_name':'sns_api4','email_address':'test@holmescentral.co.uk'}

data = {
	"first_name": "vs_SNS_API1",
	"email_address": "test@holmescentral.co.uk"
}



# response = get(BASE_URL + "/get-topics")
# print(response.text)

response = post(BASE_URL + "/send", json = data)
print(response.text)


