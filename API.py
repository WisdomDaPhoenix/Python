#base_url = "http://demo.codingnomads.co:8080/tasks_api/users" returns
#a 200 status code (successful) because API has a /users endpoint, the /users
#endpoint exists and the request to the server was successful

#base_url = "http://demo.codingnomads.co:8080/tasks_api/developers" returns a
#404 status code(client error) because the API does not have a /developers endpoint

import requests
from pprint import pprint
myparams = {"id": 5,
"first_name": "Martin",
"last_name": "Breuss",
"email": "martin@email.com"
            }
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params = myparams)
print(response.status_code)
pprint(response.content)

"""



import requests
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
print(f"{response.content}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Encoding: {response.encoding}")
print(f"Response URL: {response.url}")


import requests
myparams = {
    "email": "caden@email.com"
}
pic = requests.get("http://randomfox.ca/floof")
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=myparams)
print(pic.text)
print(response.status_code)




import requests
myparams = {'id': '3','first_name': 'Caden5','email': 'caden@email.com'}
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params = myparams)
print(response.status_code)

import requests
base_url = "http://demo.codingnomads.co:8080/tasks_api/developers"
response = requests.get(base_url)
print(response.status_code)

s = 'abcdefghijklmnopqrstuvwxyz'
M = list(s)
#print(M)
final = []
for i in range(len(M)):
    final.append(M[i]*(i+1))

print(final)"""
    
    


