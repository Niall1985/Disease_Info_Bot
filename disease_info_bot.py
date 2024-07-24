from flask import Flask, render_template, request
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-pro")

with open('disease_database.json', 'r') as file:
    database = json.load(file)

app = Flask(__name__, static_folder='static')

def get_disease_info(disease_name):
    for category in database:
        for disease in category['diseases']:
            if disease['name'].lower() == disease_name.lower():
                return disease
    return None

def generate_additional_content(prompt):
    response = model.generate_content(prompt)
    if hasattr(response, 'text'):
        return response.text
    elif hasattr(response, 'content'):
        return response.content
    else:
        return 'No additional content available'
    
def generate_extract_disease_name(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def formatted_result(disease, additional_content):
    return f"""
Disease Information:
---------------------
Name: {disease['name']}

Description:
{disease['description']}

Transmission:
{disease['transmission']}

Symptoms:
{disease['symptoms']}

Treatment:
{disease['treatment']}

Complications:
{disease['complications']}

Prevention:
{disease['prevention']}

Additional Information:
-----------------------
{additional_content}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['query'].strip().lower()
        prompt = f"Extract the disease name from the following text and return only the disease name in lowercase: '{user_input}'"
        
        # Process the input to get the disease information
        reply = generate_extract_disease_name(prompt)
        disease_info = get_disease_info(reply)
        
        if disease_info:
            additional_prompt = f"Provide more information about risk factors and diagnosis of {user_input} in the format Risk Factors: (content) and on the next line Diagnosis: (content)."
            additional_content = generate_additional_content(additional_prompt)
            result = formatted_result(disease_info, additional_content)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
