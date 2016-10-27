import click
from time import sleep
import psutil
import os

status = "Not loaded."
process = None

@click.group()
def cli():
    """ Command line interface for the Bonsai Artificial Intelligence Engine.
    """
    pass

@click.command()
@click.argument('key',required=False)
def configure(key=None):
    """ Authenticate with the BRAIN Server.
    """
    if not key:
        click.echo("You can get the access key at "
                   "https://beta.bons.ai/accesskey")
        click.prompt("Secret Key (typing will be hidden)", hide_input=True)
        click.echo("Successfully authenticated.")

@click.group()
def brain():
    """ Create, list, and delete BRAINs
    """
    pass

@click.command("list")
def brain_list():
    """ Lists BRAINs owned by current user or by the user under a given URL.
    """
    click.echo("MyBrain")

@click.command("create")
@click.argument("brainname")
def brain_create(brainname):
    """ Create a new BRAIN.
    """
    click.echo("Creating MyCartpole... done.")
    click.echo("https://beta.bons.ai/cksbonsai/MyBRAIN")
    click.echo("Added MyBRAIN to project file.")

@click.command("destroy")
@click.argument("brainname")
def brain_destroy(brainname):
    """ Destroys a BRAIN owned by current user or by the user under a given 
        URL.
    """
    click.prompt("Please retype the name of the BRAIN")
    click.echo("Deleted {0}".format(brainname))

@click.group()
def project():
    """ Manipulate the Bonsai project file.
    """
    pass

@click.command("add-brain")
@click.argument("brainname")
def add_brain(brainname):
    """ Adds a BRAIN to the project in the local directory.
    """
    click.echo("Added {0} to project file.".format(brainname))

@click.command("create")
def create_project():
    """ Creates an empty project file in the local directory.
    """
    click.echo("Added project file.")

@click.command()
def load():
    """ Loads project into BRAIN
    """
    click.echo("Loaded mountaincar.bproj into MyBRAIN.")
    click.echo("Run 'bonsai train start' to start training.")

@click.group()
def train():
    """ Start and stop training on the BRAIN.
    """
    pass

@click.command("start")
def train_start():
    click.echo("training started.")
    click.echo("See https://beta.bons.ai/cksbonsai/MyBrain for status.")
    click.echo("Starting simulator...")
    fnull = open(os.devnull, 'w')
    psutil.Popen(["python", "mountaincar_simulator.py"],stderr=fnull)

    click.echo("Training started.")

@click.command("stop")
def train_stop():
    for p in psutil.process_iter():
        try:
            if "mountaincar_simulator.py" in p.cmdline():
                p.kill()
        except:
            pass
    click.echo("Training stopped.")
    click.echo("Connect to wss://api.bons.ai/cksbonsai/MyBrain/12 for predictions.")

@click.command()
def status():
    """ Displays the status of the current BRAIN.
    """
    click.echo("{0}".format(status))

@click.command()
def log():
    """ Returns a log of any errors triggered on the server.
    """
    click.echo("No errors.")

@click.group()
def sims():
    """ Simulator connection state, data transmitted, etc
    """
    pass

@click.command("list")
def sims_list():
    """ List the simulators connected to the BRAIN server.
    """
    click.echo("NAME\t\tINSTANCES\tSTATUS")
    click.echo("breakout\t1\t\tready")

cli.add_command(configure)
cli.add_command(brain)
cli.add_command(sims)
cli.add_command(load)
cli.add_command(status)
cli.add_command(train)
cli.add_command(project)
project.add_command(add_brain)
project.add_command(create_project)
train.add_command(train_start)
train.add_command(train_stop)
brain.add_command(brain_list)
brain.add_command(brain_create)
brain.add_command(brain_destroy)
sims.add_command(sims_list)

if __name__ == "__main__":
    cli()
