import  wikipedia

def scrape(name="Microsoft", length=5):
    result = wikipedia.summary(name, sentences=length)
    return result

print(scrape("wikipedia"))







#import click
#from mylib.bot import scrape


#@click.command()
#@click.option("--name", help="Web page we want to scrape")
#def cli(name):
#    result = scrape(name)
#    click.echo(click.style(f"{result}:", fg="blue"))


#if __name__ == "__main__":
#    cli()