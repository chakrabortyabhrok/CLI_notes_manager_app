class Notes:

    def __init__(self, id, title, description, priority):
        self.id = int(id)
        self.title = title
        self.description = description
        self.priority = priority

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority
        }
        
    def display_notes(self):
        return (f"{self.id:<3} | {self.title:<11} | {self.description:<25} | {self.priority:<12}")