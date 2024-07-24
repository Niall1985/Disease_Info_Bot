import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-pro")

with open('disease_data.json', 'r') as file:
    database = json.load(file)

def get_disease_info(disease_name):
    for category in database:
        for disease in category['diseases']:
            if disease['name'].lower() == disease_name.lower():
                return disease
    return None

def generate_additional_content(prompt):
    response = model.generate_content(prompt)
    # print("Response object:", response)
    if hasattr(response, 'text'):
        return response.text
    elif hasattr(response, 'content'):
        return response.text
    else:
        return 'No additional content available'

def formatted_result(disease, additional_content):
    return f"""
    Disease Information:
    ---------------------
    Name: {disease['name']}
    Description: {disease['description']}
    Transmission: {disease['transmission']}
    Symptoms: {disease['symptoms']}
    Treatment: {disease['treatment']}

    Additional Information:
    -----------------------
    {additional_content}
    """

user_input = input("Enter your queries:").strip()
disease_info = get_disease_info(user_input)

if disease_info:
    additional_prompt = f"Provide more information about {user_input}."
    additional_content = generate_additional_content(additional_prompt)
    final_response = formatted_result(disease_info, additional_content)
    print(final_response)
else:
    print("Data not found")
