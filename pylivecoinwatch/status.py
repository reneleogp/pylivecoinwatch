import requests
import json

url = "https://api.livecoinwatch.com/status"

payload = {}
headers = {
    'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
