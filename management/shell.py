import click

from management import create_app


app = create_app()


@app.cli.command()
def status():
    """It seems that CLI is working fine."""
    click.echo("Flask CLI is working fine!")
