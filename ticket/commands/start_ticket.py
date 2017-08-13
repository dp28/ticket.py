from ticket.git import branch_factory
from ticket.errors import TicketError

class NotFoundError(TicketError):

    def __init__(self, entity_type, id):
        super(NotFoundError, self).__init__(
            '{type} not found with id {id}'.format(type=entity_type, id=id)
        )


def start_ticket(ticket_id, ticket_store):
    ticket = ticket_store.get_by_id(ticket_id)
    if ticket is None:
        raise NotFoundError('ticket', ticket_id)

    branch = branch_factory.create_branch(ticket.branch_name)
    ticket.start()
    ticket_store.save(ticket)

