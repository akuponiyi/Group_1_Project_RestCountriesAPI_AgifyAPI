
from pip._vendor import requests 
from pprint import pprint as pp

def predict_age(name_to_predict):

    agifyurl = f'https://api.agify.io/?name={name_to_predict}'

    response = requests.get(agifyurl)
    print(response.status_code)
    data = response.json()

    parameters = {
        'name': 'name',
        'label': 'age'
    }

    response = requests.get(url=agifyurl, params=parameters)

    if response.status_code == 200:
        age = data['age']
        print(f"The predicted age is: {age}")
    else:
        print(f"Error: {response.status_code}, {response.name}")

name_to_predict = 'Jane'
predict_age(name_to_predict)