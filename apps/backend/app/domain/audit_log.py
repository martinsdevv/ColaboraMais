class AuditLog:

    def __init__(
        self,
        user_id,
        action,
        entity,
        entity_id,
        data=None,
        id=None
    ):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.entity = entity
        self.entity_id = entity_id
        self.data = data