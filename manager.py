import os
import json
from notes import Notes

class NotesManager:
    def __init__(self):
        self._notes = []
        self.id = 
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(BASE_DIR, "notes.json")

    def load_notes(self):
        if not os.path.exists(self.file_name):
            print("-- File Not Found --")
    
        try:
            with open (self.file_name, "r") as file:
                json.load(file)
                print(f"Loaded {len(self.file_name)}")
        except json.JSONDecodeError as e:
            print(f"Error Loading: {e}")

    def save_notes(self):
        data = [
            {"id": }
        ]
        with open (self.file_name, "w") as file:
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

    def get_notes_by_priority(notes, level):
        return[n for n in notes if n["notes_info"]["priority"] == level]


def print_notes(self):
    if not notes:
        print("-- No Notes Added --\n")
        return    
    print(" ID |    TITLE    |        DESCRIPTION        |  PRIORITY  ")
    print("-" * 55)
    for n in notes:
        print(f"{n['id']:<3} | {n['notes_info']['title']:<11} | {n['notes_info']['description']:<25} | {n['notes_info']['priority']:<12}")
    print("-" * 55)

