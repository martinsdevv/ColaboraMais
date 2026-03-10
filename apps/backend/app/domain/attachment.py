class Attachment:

    def __init__(
        self,
        ticket_id,
        file_path,
        file_type,
        id=None
    ):
        self.id = id
        self.ticket_id = ticket_id
        self.file_path = file_path
        self.file_type = file_type