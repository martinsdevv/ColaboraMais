class User:

    def __init__(
        self,
        name,
        email,
        password_hash,
        role_id,
        active=True,
        id=None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role_id = role_id
        self.active = active