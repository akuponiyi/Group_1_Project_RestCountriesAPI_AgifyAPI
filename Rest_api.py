# Import necessary libraries
from pip._vendor import requests #Library for making HTTP requests
from pprint import pprint as pp # Pretty-print library for formatting output
import json # Import the JSON library for working with JSON data

# Define a function to retrieve country data from the REST Countries API by name
def get_country_data_by_name(country_name):
    
    # Make an HTTP request to the API
        response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')

    # Check if the request was successful
        if response.status_code == 200:
            # Get the country data from the response
            data = response.json()
            
            with open('country_list.txt','w') as text_file:

            # Extract the required parameters and return them as a dictionary
                # --- Construct a formatted message using f-strings for readability ---
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
                text_file.write(message) # --- Write the formatted message to the text file ---
                # return country_data
            
             # --- Handle unsuccessful requests by printing an error message ---
        else:
            print(f"Failed to fetch country data. Status code: {response.status_code}")
            return {} # Return an empty dictionary on failure
    

# Example usage:
        # --- Prompt the user to enter a country name ---
country_name = input('Enter country of choice: ') # Get input from the user
# --- Retrieve country data from the API ---
data = get_country_data_by_name(country_name) # Call the function to fetch data
print(data)



    



