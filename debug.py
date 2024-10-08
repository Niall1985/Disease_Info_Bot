# # import spacy

# # # Load English tokenizer, tagger, parser and NER
# # nlp = spacy.load("en_core_web_sm")

# # # Process whole documents
# # text = ("provide me some information about diabetes")
# # doc = nlp(text)

# # # Analyze syntax
# # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

# import spacy

# # Load English tokenizer, tagger, parser, and NER
# nlp = spacy.load("en_core_web_sm")

# # Process the document
# text = "provide me some information about diabetes"
# doc = nlp(text)

# # Extract named entities
# entities = [ent.text for ent in doc.ents]
# print("Named entities:", entities)

# import google.generativeai as genai
# import dotenv
# from dotenv import load_dotenv
# import os
# load_dotenv()
# key = os.getenv('key')  
# genai.configure(api_key=key)
# model = genai.GenerativeModel(model_name="gemini_pro")
# user_prompt = input("Enter your query: ")
# def generate_extract_disease_name(prompt):
#     response = model.generate_content(prompt)
#     return response.text.strip()  
# prompt = f"Extract the disease name from the following text and return only the disease name in lowercase: '{user_prompt}'"
# reply = generate_extract_disease_name(prompt)
# print("Extracted Disease Name:", reply)

import json
def to_lowercase(data):
    if isinstance(data, dict):
        return {k: to_lowercase(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_lowercase(item) for item in data]
    elif isinstance(data, str):
        return data.lower()
    else:
        return data

def convert_json_to_lowercase(input_file_path, output_file_path):
    try:
        # Read the JSON file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    
        lowercased_data = to_lowercase(data)
    
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(lowercased_data, file, ensure_ascii=False, indent=4)
        
        print("Conversion complete. Check the output file.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with the path to your input and output JSON files
input_file_path = ""
output_file_path = ""

convert_json_to_lowercase(input_file_path, output_file_path)
