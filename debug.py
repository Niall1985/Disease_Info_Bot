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
