from pip._vendor import requests 
from pprint import pprint as pp
import json


def get_country_data_by_name(country_name):
    
    # Make an HTTP request to the API
        response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')

    # Check if the request was successful
        if response.status_code == 200:
            # Get the country data from the response
            data = response.json()

            # if not country_list:
            #     print(f"No data found for {country_name}")
            #     return {}

            # Use the first country in the list
            # data = country_list[0]
            with open('country_list.txt','w') as text_file:
            # Extract the required parameters and return them as a dictionary
                message = "{name} is a good location for vacation with a population of {population} and a timezone of {timezones}.\nThe capital of {name} is {capital}. It is located under the {continents} continent. \nThe major language spoken is {languages}. The region in {name} is {region} while the subregion is {subregion}.\nAs a result of its state of independence being {independence}, it is {status}.\nThe currency used in {name} is {currencies}.".format(
                    name = data[0]['name']['official'],
                    timezones = ", ".join(data[0]['timezones']),
                    capital = data[0]['capital'][0],
                    independence = data[0]['independent'],
                    status = data[0]['status'],
                    languages = data[0]['languages'],
                    currencies = data[0]['currencies'],
                    continents = data[0]['continents'][0],
                    population = data[0]['population'],
                    region = data[0]['region'],
                    subregion = data[0]['subregion']
                )
                text_file.write(message)
                # return country_data
            
            
        else:
            print(f"Failed to fetch country data. Status code: {response.status_code}")
            return {}
    

# Example usage:
country_name = input('Enter country of choice: ')
data = get_country_data_by_name(country_name)
print(data)



    



