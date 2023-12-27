
from pip._vendor import requests 
from pprint import pprint as pp

agifyurl = 'https://api.agify.io/?name=michael' 

response = requests.get(agifyurl)
print(response.status_code)
data = response.json()