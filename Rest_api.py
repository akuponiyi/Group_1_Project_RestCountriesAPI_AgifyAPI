from pip._vendor import requests 
from pprint import pprint as pp
import json

restcountries_url = 'https://restcountries.com/v3.1/name/Kenya?fullText=true' 

response = requests.get(restcountries_url)
print(response.status_code)
data = response.json()
