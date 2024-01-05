from pip._vendor import requests 
from pprint import pprint as pp
import json

restcountries_url = 'https://restcountries.com/v2/all'

response= requests.get(restcountries_url) 

data=response.json()

# check data type
print(type(data))
print(data)

# using for loop, this will give detail of each country
# for country in data:
#     print(country['name'] , country['population'])

# ask user what is there name and what country they are staying in
print("What is your name?")
username = input()
print("Which country do you stay in?")
user_country = input()

# taking the next statemnt to a new line
print("/n")

# trying to know the user's country and it's population
for country in data:
    if(country['name'])== user_country:
        print("That is wonderfull, {} !!".format(username))
        print("Your country's population is manageable, {} is not that much.".format(country['population']))
