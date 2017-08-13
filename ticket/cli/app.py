import click
from ticket.commands.start_ticket import start_ticket
from ticket.pivotal import ticket_store


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


if __name__ == '__main__':
    app()
