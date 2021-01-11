#JSON is a string but not a useable string. So we have to convert it into a
#python usable data structure e.g dictionary or list
#The .get() method and .json() method are contained in the requests module or package
#The .get() method allows us to make a HTTP request to the server for information
#The .json() method converts the response to a python dictionary which then makes it accessible
#The PPRINT function makes data structures (e.g dictionaries, lists) look more readable as against the print function
#Access format below
#There are 3 data in the main ditionary i. data ii. error iii. statusCode
#Name of dictionary - [data key (like error or statusCode key Access)] - [Index of listed JSON Object] - [Key of item to be accessed]

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()

size = len(data["data"])
print(size)
print(data["error"])
print(data["statusCode"])
pprint(data["data"])

"""

print()
print(data["data"][105]["id"])
print()
print(data["data"][102]["first_name"])
print(data["data"][102]["last_name"])
print(data["data"][102]["email"])
print()
print(data["data"][2]["first_name"])
print()
print(data["data"][2]["last_name"])
print()
print(data["data"][2]["email"])"""

