from email.policy import default
import click

from libs import hello

@click.command()
@click.option('--name', '-n', 
    type=str, required=False, 
    default=__file__
)
def main(name):
    hello.hello_from(name)

if __name__ == '__main__':
    main()
