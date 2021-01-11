
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[YOUR FIRST NAME FIELD]",
    "last_name": "[STANLEY AMAECHI]",
    "email": "[YOUR EMAIL ADDRESS]"

    }

response = requests.post(base_url, json=body)

print(f"Response StatusCode: {response.status_code}")

response = requests.get(base_url)

print(f"Response Content: {response.content}")












