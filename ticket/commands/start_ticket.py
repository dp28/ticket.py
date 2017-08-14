from ticket.git import branch_factory
from ticket.git import repos
from ticket.errors import TicketError


class NotFoundError(TicketError):

    def __init__(self, entity_type, id):
        super(NotFoundError, self).__init__(
            '{type} not found with id {id}'.format(type=entity_type, id=id)
        )


def start_ticket(ticket_id, ticket_store, pull_request_factory, pull_store):
    ticket = ticket_store.get_by_id(ticket_id)
    if ticket is None:
        raise NotFoundError('ticket', ticket_id)

    repo = repos.get_current()
    branch = branch_factory.create_branch(ticket.branch_name)
    pull_request = pull_request_factory.create_pull_request(branch, repo)
    ticket.start()
    ticket.add_pull_request(pull_request)
    pull_store.save(pull_request)
    ticket_store.save(ticket)
