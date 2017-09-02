import click
from ticket.commands.start_ticket import start_ticket
from ticket.commands.create_pull_request import create_pull_request
from ticket.pivotal import ticket_store
from ticket.github import pull_request_store, pull_request_factory



@click.group()
def app():
    pass


@app.command()
def run():
    click.echo('Hello, ticket')


@app.command()
@click.argument('ticket_id')
def start(ticket_id):
    start_ticket(ticket_id, ticket_store)


@app.command()
def create_pull():
    create_pull_request(
        ticket_store,
        pull_request_factory,
        pull_request_store
    )


if __name__ == '__main__':
    app()
