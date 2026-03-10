class Ticket:
    def __init__(self, title, description, author_id, department_target_id, status="open", id=None):
        self.id = id
        self.title = title
        self.description = description
        self.author_id = author_id
        self.department_target_id = department_target_id
        self.status = status