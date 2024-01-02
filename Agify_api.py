
from pip._vendor import requests 
from pprint import pprint as pp

def predict_age(name_to_predict):
    with open('group_members_age_prediction.txt','w') as text_file:
        for name in name_to_predict:
            agifyurl = f'https://api.agify.io/?name={name}'
            response = requests.get(url=agifyurl)
 
            if response.status_code == 200:
                data = response.json()
                pp(data)
 
                message = "At {count} count, the API predicted {name}'s age as: {age}\n".format(
                    count = data['count'],
                    name = data['name'],
                    age = data['age']
                )      
                text_file.write(message)
            else:
                print(f"Error: {response.status_code}, {response.name}")
 
name_to_predict = ['Busayo', 'Jesulolufemi', 'Lolu', 'Ahmed', 'Fadipe', 'Rasheed', 'Kate', 'Janetoms', 'Oketch', 'Oluwatayo', 'Ameh', 'Omobolanle', 'Fatima', 'Janet', 'Blessing', 'Precious']
predict_age(name_to_predict)