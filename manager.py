import os
import json
from notes import Notes

class NotesManager:

    def __init__(self):
        self._notes = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(BASE_DIR, "notes.json")

    def load_notes(self):
        if not os.path.exists(self.file_name):
            print("-- File Not Found --")
    
        try:
            with open (self.file_name, "r") as file:
                raw_data = json.load(file)

                self._notes = []

                for n in raw_data:
                    new_obj = Notes(
                        id=n["id"],
                        title=n["title"],
                        description=n["description"],
                        priority=n["priority"]
                    )
                    self._notes.append(new_obj)

                print(f"\nLoaded: {len(self.file_name)} notes")

        except json.JSONDecodeError as e:
            print(f"Error Loading: {e}")

    def save_notes(self):
        data = [n.to_dict() for n in self._notes]
        with open (self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def get_new_id(self):
        for n in self._notes:
            if not n:
                return 1
        else:
            return max(n["id"]for n in self._notes ) + 1
    
    def add_notes(self, notes_title, notes_description, notes_priority):
        new_note = {
            "id": self.get_new_id(),
            "notes_info": {
            "title": notes_title,
            "description": notes_description,
            "priority": notes_priority
            }
        }
        self._notes.append(new_note)

    def delete_notes(self, note_id):
        for n in self._notes:
            if n["id"] == note_id:
                self._notes.remove(n)
                return True
        return False

    def get_notes_by_priority(self, level):
        return[n for n in self._notes if n["notes_info"]["priority"] == level]


    def print_notes(self):
        if not self._notes:
            print("-- No Notes Added --\n")
            return    
        print(" ID |    TITLE    |        DESCRIPTION        |  PRIORITY  ")
        print("-" * 55)
        for n in self._notes:
            print(f"{n['id']:<3} | {n['notes_info']['title']:<11} | {n['notes_info']['description']:<25} | {n['notes_info']['priority']:<12}")
        print("-" * 55)

