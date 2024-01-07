# Import necessary libraries
from pip._vendor import requests #Library for making HTTP requests
from pprint import pprint as pp # Pretty-print library for formatting output


# Function to predict ages and save results to a text file
def predict_age(name_to_predict):
    """Predicts ages for a list of names using the Agify API and writes results to a text file.

   Args:
       name_to_predict (list): A list of names to predict ages for.
   """
    with open('group_members_age_prediction.txt','w') as text_file: # Open text file for writing
        for name in name_to_predict: 
            agifyurl = f'https://api.agify.io/?name={name}' # Construct API URL with name
            response = requests.get(url=agifyurl) # Send GET request to API
 
            if response.status_code == 200: # Check for successful response
                data = response.json() # Parse JSON response
                pp(data) # Pretty-print data to text file

 # Extract relevant data and format message
                message = "At {count} count, the API predicted {name}'s age as: {age}\n".format(
                    count = data['count'], # Number of people in the dataset with the given name
                    name = data['name'], # The name for which the prediction was made
                    age = data['age'] # The predicted age
                )      
                text_file.write(message) # Write formatted message to text file
            else:
                print(f"Error: {response.status_code}, {response.name}") # Print error message

 # List of names to predict ages for
name_to_predict = ['Busayo', 'Jesulolufemi', 'Lolu', 'Ahmed', 'Fadipe', 'Rasheed', 'Kate', 'Janetoms', 'Oketch', 'Oluwatayo', 'Ameh', 'Omobolanle', 'Fatima', 'Janet', 'Blessing', 'Precious']
# Call the function to predict ages and save results
predict_age(name_to_predict)