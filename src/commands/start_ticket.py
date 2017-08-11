from src.git.branch import Branch


class TicketError(Exception):
    pass


class NotFoundError(TicketError):

    def __init__(self, entity_type, id):
        super(NotFoundError, self).__init__(
            '{type} not found with id {id}'.format(type=entity_type, id=id)
        )


def start_ticket(ticket_id, ticket_store, branch_store):
    ticket = ticket_store.get_by_id(ticket_id)
    if ticket is None:
        raise NotFoundError('ticket', ticket_id)

    branch = Branch(ticket.get_branch_name())
    branch_store.create(branch)
