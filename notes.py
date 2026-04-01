class Notes:

    def __init__(self, id, title, description, priority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority

    def to_dict(self):
        return[
            {
                "id": 1,
                "notes_info": {
                    "title": "Milk",
                    "description": "Buy 2L whole milk",
                    "priority": "High"
                    }
            }
        ]
    
    def display_notes(self):
        return (f"{self.id:<3} | {self.title:<11} | {self.description:<25} | {self.priority:<12}")