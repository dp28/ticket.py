from ticket.git import branch_store, repos


def create_pull_request(ticket_store, pull_factory, pull_store):
    ticket = ticket_store.get_current()
    repo = repos.get_current()
    pull_request = pull_factory.create_pull_request(ticket, repo)
    ticket.start()
    pull_store.save(pull_request)
    ticket.add_pull_request(pull_request)
    ticket_store.save(ticket)
    print('Created {pull} and added it to {ticket}'.format(
        pull=pull_request.url,
        ticket=ticket.url
    ))
