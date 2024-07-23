import spacy
nlp = spacy.load("en_core_web_sm")
def extract_content(command):
    doc = nlp(command)
    # Print recognized entities for debugging
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")
# # Test the function
print(extract_content('Diabetes'))