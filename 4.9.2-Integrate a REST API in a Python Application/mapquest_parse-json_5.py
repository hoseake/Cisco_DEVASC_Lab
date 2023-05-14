import requests
import urllib.parse
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QLExbgSj5oKujvqQq7C7SHYrabQAE34P"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if orig == "quit" or orig == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from": orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        # print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")