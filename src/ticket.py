import click

@click.group()
def ticket():
    pass

@ticket.command()
def run():
    click.echo('Hello, ticket')

if __name__ == '__main__':
    ticket()
