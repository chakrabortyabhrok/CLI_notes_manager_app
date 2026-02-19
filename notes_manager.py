import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME =os.path.join(BASE_DIR, "notes.json")

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

def get_new_id(notes):
    if not notes:
        return 1
    else:
        return max(n["id"]for n in notes ) + 1
    
def add_notes(notes, notes_title, notes_description, notes_priority):
    new_note = {
        "id": get_new_id(notes),
        "notes_info": {
            "title": notes_title,
            "description": notes_description,
            "priority": notes_priority
        }
    }
    notes.append(new_note)

def delete_notes(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return True
    return False


def show_ALL_priority(notes):
    return [n["priority"] for n in notes]

def show_HIGH_priority(notes):
    return [n for n in notes if n["priority"] == "High"]

def show_MEDIUM_priority(notes):
    return [n for n in notes if n["priority"] == "Medium"]

def show_LOW_priority(notes):
    return [n for n in notes if n["priority"] == "Low"]
