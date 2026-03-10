class TicketReply:

    def __init__(
        self,
        ticket_id,
        author_id,
        message,
        type,
        id=None
    ):
        self.id = id
        self.ticket_id = ticket_id
        self.author_id = author_id
        self.message = message
        self.type = type