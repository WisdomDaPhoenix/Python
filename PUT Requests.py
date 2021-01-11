import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 213,
    "first_name": "Faith",
    "last_name": "Macwen",
    "email": "faith_macwen@gmail.com"

    }

response = requests.put(url, json=body)
print(f"Response StatusCode: {response.status_code}")

response = requests.get(url)

print(f"Response Content: {response.content}")
