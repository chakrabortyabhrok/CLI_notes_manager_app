class Notes:

    def __init__(self, id, title, description, priority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority

    def to_dict(self):
        return{
            "id":self.id,
            "notes_info": {
                "title": self.title,
                "description": self.description,
                "priority": self.priority
            }
        }
    