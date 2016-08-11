import click
from time import sleep

@click.group()
def cli():
    pass

@click.command()
def configure():
    """ Authenticates the local command with the BRAIN Server.
    """
    click.echo("You can get the access key at https://brains.bons.ai/accesskey")
    click.prompt("Secret Key", hide_input=True)
    click.echo("Successfully authenticated.")

@click.group()
def brain():
    pass

@click.command("list")
def brains_list():
    """ Lists BRAINs owned by current user or by the user under a given URL.
    """
    click.echo("myBRAIN")

@click.command()
@click.argument('brain', nargs=1)
@click.argument('filenames', nargs=-1)
def load(brain, filenames):
    """ Loads filename into BRAIN.
    """
    click.echo("loaded.")
    click.echo("Connect simulators to wss://api.bons.ai/cksbonsai/myBRAIN for training.")

@click.command()
@click.argument("name")
def train(name):
    """ Trains a brain named NAME.
    """
    click.echo("training started.")
    click.echo("See https://brains.bons.ai/cksbonsai/myBRAIN for status.")
    click.echo("Training...")
    for trials in range(0, 100, 10):
        click.echo("{0} trials".format(trials))
        sleep(2)
    click.echo("Train complete.")
    click.echo("Connect to wss://api.bons.ai/cksbonsai/myBRAIN/12 for predictions.")

@click.group()
def sims():
    pass

@click.command("list")
def sims_list():
    click.echo("NAME\t\tINSTANCES\tSTATUS")
    click.echo("breakout\t1\t\tready")

cli.add_command(configure)
cli.add_command(brain)
cli.add_command(sims)
brain.add_command(load)
brain.add_command(train)
brain.add_command(brains_list)
sims.add_command(sims_list)

if __name__ == "__main__":
    cli()
