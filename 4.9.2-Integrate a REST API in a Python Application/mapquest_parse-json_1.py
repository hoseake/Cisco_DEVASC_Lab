import requests
import urllib.parse
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "QLExbgSj5oKujvqQq7C7SHYrabQAE34P"
url = main_api + urllib.parse.urlencode({"key":key, "from": orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)