# from pip._vendor import requests 
# from pprint import pprint as pp
# import json

# restcountries_url = 'https://restcountries.com/v3.1/name/Kenya?fullText=true' 

# response = requests.get(restcountries_url)
# print(response.status_code)
# data = response.json()


from pip._vendor import requests

def get_country_data_by_name(country_name):
    # Make an HTTP request to the API
    response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')

    # Check if the request was successful
    if response.status_code == 200:
        # Get the country data from the response
        country_list = response.json()

        if not country_list:
            print(f"No data found for {country_name}")
            return {}

        # Use the first country in the list
        country = country_list[0]

        # Extract the required parameters and return them as a dictionary
        country_data = {
            'name': country['name']['common'],
            'capital': country.get('capital', ['N/A'])[0],
            'region': country.get('region', 'N/A'),
            'language': [language for language in country.get('languages', {}).values()],
            'currencies': country.get('currencies', {}).get('KES', {}).get('name', 'N/A')
        }
        return country_data
    else:
        print(f"Failed to fetch country data. Status code: {response.status_code}")
        return {}

# Example usage:
country_name = 'Nigeria'
country_data = get_country_data_by_name(country_name)
print(country_data)
