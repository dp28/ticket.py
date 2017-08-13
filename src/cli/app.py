import click


@click.group()
def app():
    pass


@app.command()
def run():
    click.echo('Hello, ticket')


if __name__ == '__main__':
    app()
