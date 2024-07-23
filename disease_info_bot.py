import json

with open('disease_data.json', 'r') as file:
    database = json.load(file)

def get_disease_info(disease_name):
    for category in database:
        for disease in category['diseases']:
            if disease['name'].lower() == disease_name.lower():
                return disease
    return None


def formatted_result(disease):
    return f"""
    Disease Information:
    ---------------------
    Name: {disease['name']}
    Description: {disease['description']}
    Transmission: {disease['transmission']}
    Symptoms: {disease['symptoms']}
    Treatment: {disease['treatment']}
    """

user_input = input("Enter your queries:")
result = get_disease_info(user_input)


if result:
    print(formatted_result(result))
else:
    print("Data not found")
