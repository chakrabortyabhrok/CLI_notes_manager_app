from manager import NotesManager
from notes import Notes

MENU = """
Add New Note           - a
Delete Note            - d
Show All Notes         - s
Show Notes by priority - p
Exit App               - e
"""
def main():
    manager = NotesManager()
    manager.load_notes()
    print("-- Welcome to the NOTES MANAGER ! --")

    while True:
        print(MENU)
        choice = input("Enter a choice: \n").lower().strip()

        if choice == "a":
            print("-- ADD NOTE --\n")
            title = input("-- TITLE: (11 characters) --\n").strip().capitalize()
            description = input("-- DECRIPTION: (25 characters) --\n").strip().capitalize()
            priority = input("-- PRIORITY: --[High / Medium / Low]\n").strip().capitalize()

            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"

            new_id = manager.get_new_id()

            new_obj = Notes(new_id, title, description, priority)
            manager.add_notes(new_obj)

        elif choice == "d":
            print("-- DELETE NOTE --\n")
            try:
                note_id = int(input("Enter the note ID: \n"))
                if manager.delete_notes(note_id):
                    manager.save_notes()
                    print("-- Note Deleted --")
                else:
                    print("-- ID not found --")

            except ValueError:
                print("-- Enter a valid ID --\n")
            
        elif choice == "s":
            print("-- ALL NOTES --")
            manager.print_notes()

        elif choice == "p":
            print("-- SEARCH NOTES BY PRIORITY --")
            level = input("Enter the priority level: --[High / Medium / Low]\n").strip().capitalize()

            if level not in ["High", "Medium", "Low"]:
                print(f"-- No notes found with priority: {level}")
                
            else:
                manager.get_notes_by_priority(level)

        elif choice == "e":
            print("-- Goodbye --")
            break

        else:
            print("-- Enter a valid choice. --")


if __name__ == "__main__":
    main()
