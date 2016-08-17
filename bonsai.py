import click
from time import sleep

@click.group()
def cli():
    """ Command line interface for the Bonsai Artificial Intelligence Engine.
    """
    pass

@click.command()
def configure():
    """ Authenticate with the BRAIN Server.
    """
    click.echo("You can get the access key at https://brains.bons.ai/accesskey")
    click.prompt("Secret Key (typing will be hidden)", hide_input=True)
    click.echo("Successfully authenticated.")

@click.group()
def brains():
    """ Create, load, train BRAINs
    """
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
    """ Loads FILENAMES into BRAIN.
    """
    click.echo("loaded.")
    click.echo("Connect simulators to wss://api.bons.ai/cksbonsai/myBRAIN for training.")

@click.command()
@click.argument("brainname")
def train(brainname):
    """ Trains BRAINNAME
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
    """ Simulator connection state, data trasmitted, etc
    """
    pass

@click.command("list")
def sims_list():
    """ List the simulators connected to the BRAIN server.
    """
    click.echo("NAME\t\tINSTANCES\tSTATUS")
    click.echo("breakout\t1\t\tready")

cli.add_command(configure)
cli.add_command(brains)
cli.add_command(sims)
brains.add_command(load)
brains.add_command(train)
brains.add_command(brains_list)
sims.add_command(sims_list)

if __name__ == "__main__":
    cli()
