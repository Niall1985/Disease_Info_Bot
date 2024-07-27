from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
key = os.getenv('key')

# Configure Generative AI model
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-pro")

# Load the disease database
with open('disease_database.json', 'r') as file:
    database = json.load(file)

app = Flask(__name__, static_folder='static')

# Initialize chat history
chat_history = []

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
    global chat_history
    user_query = None
    result = None
    waiting = False

    if request.method == 'POST':
        data = request.json
        user_query = data.get('query', '').strip()
        prompt = f"Extract the disease name from the following text and return only the disease name in lowercase: '{user_query}'"

        waiting = True
        reply = generate_extract_disease_name(prompt)
        disease_info = get_disease_info(reply)
        
        if disease_info:
            additional_prompt = f"Provide more information about risk factors and diagnosis of {user_query} in the format Risk Factors: (content) and on the next line Diagnosis: (content)."
            additional_content = generate_additional_content(additional_prompt)
            result = formatted_result(disease_info, additional_content)

        waiting = False

        # Add new query and response to chat history
        chat_history.append({'query': user_query, 'response': result})

        return jsonify({'response': result})

    return render_template('index.html', chat_history=chat_history, waiting=waiting)

if __name__ == '__main__':
    app.run(debug=True)
