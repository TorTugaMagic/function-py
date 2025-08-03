import click
from mylib.bot import scrape
#import  wikipedia

#from mylib.bot import scrape
# click.echo

@click.command()
@click.option("--name", prompt="wikipedia page to scrape",
                help='Web page we want to scrape')
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="red", bg="blue"))

if __name__ == "__main__":
   cli()