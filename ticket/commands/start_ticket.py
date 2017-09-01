from ticket.git import branch_store
from ticket.git import repos
from ticket.errors import TicketError


class NotFoundError(TicketError):

    def __init__(self, entity_type, id):
        super(NotFoundError, self).__init__(
            '{type} not found with id {id}'.format(type=entity_type, id=id)
        )


def start_ticket(ticket_id, ticket_store, pull_factory, pull_store):
    ticket = ticket_store.get_by_id(ticket_id)
    if ticket is None:
        raise NotFoundError('ticket', ticket_id)

    repo = repos.get_current()
    branch = branch_store.create_branch(ticket.branch)
    pull_request = pull_factory.create_pull_request(ticket, repo)
    ticket.start()
    pull_store.save(pull_request)
    ticket.add_pull_request(pull_request)
    ticket_store.save(ticket)
