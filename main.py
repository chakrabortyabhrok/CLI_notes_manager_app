from manager import NotesManager

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
            title = input("-- TITLE: (11 characters) --\n").lower().strip()
            description = input("-- DECRIPTION: (25 characters) --\n").lower().strip()
            priority = input("-- PRIORITY: --[High / Medium / Low]\n").lower().strip().capitalize()

            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"
            
            manager.add_notes(notes, title, description, priority)
            manager.save_notes(notes)
            print("-- Notes Added --")

        elif choice == "d":
            print("-- DELETE NOTE --\n")
            try:
                note_id = int(input("Enter the note ID: \n"))
                if manager.delete_notes(notes, note_id):
                    manager.save_notes(notes)
                    print("-- Note Deleted --")
                else:
                    print("-- ID not found --")

            except ValueError:
                print("-- Enter a valid ID --\n")
            
        elif choice == "s":
            print("-- ALL NOTES --")
            manager.print_notes(notes)

        elif choice == "p":
            print("-- SEARCH NOTES BY PRIORITY --")
            level = input("Enter the priority level: --[High / Medium / Low]\n").lower().strip().capitalize()

            if level not in ["High", "Medium", "Low"]:
                print("-- no notes with aked priority --")
            manager.print_notes(manager.get_notes_by_priority(notes, level))

        elif choice == "e":
            print("-- Goodbye --")
            break

        else:
            print("-- Enter a valid choice. --")


if __name__ == "__main__":
    main()
