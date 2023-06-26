import requests

# Getting the json data from the open trivia database

otd_url = "https://opentdb.com/api.php"
otd_parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url=otd_url, params=otd_parameters)

data = response.json()

