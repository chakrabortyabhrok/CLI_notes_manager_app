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

def get_notes_by_priority(notes, level):
    return[n for n in notes if n["notes_info"]["priority"] == level]

MENU = """

Add New Note           - a
Delete Note            - d
Show All Notes         - s
Show Notes by priority - p
Exit App               - e

"""
def print_notes(notes):
    if not notes:
        print("-- No Notes Added --\n")
        return    
    print(" ID |    TITLE    |        DESCRIPTION        |  PRIORITY  ")
    print("-" * 55)
    for n in notes:
        print(f"{n['id']:<3} | {n['notes_info']['title']:<11} | {n['notes_info']['description']:<25} | {n['notes_info']['priority']:<12}")
    print("-" * 55)

def main():
    notes = load_notes()
    print("-- Welcome to the NOTES MANAGER ! --")
    while True:
        print(MENU)
        choice = input("Enter a choice: \n").lower().strip()

        if choice == "s":
            print_notes(notes)

        elif choice == "e":
            print("-- Goodbye --")
            break

        else:
            print("-- Enter a valid choice. --")


if __name__ == "__main__":
    main()