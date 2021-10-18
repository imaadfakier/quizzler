import requests

BASE_URL = 'https://opentdb.com/api.php'

parameters = {
    'amount': 15,
    'category': 21,
    'type': 'boolean',
}

response = requests.get(url=BASE_URL, params=parameters)
response.raise_for_status()  # automatically raises bad response code exception
data = response.json()
question_data = data['results']
