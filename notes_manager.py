import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME =os.path.join(BASE_DIR, "notes.py")

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open (FILE_NAME, "r") as file:
            return json.load(file)        
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    with open (FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)