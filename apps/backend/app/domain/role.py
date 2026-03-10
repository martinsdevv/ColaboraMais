class Role:

    def __init__(
        self,
        name,
        department_id,
        id=None
    ):
        self.id = id
        self.name = name
        self.department_id = department_id