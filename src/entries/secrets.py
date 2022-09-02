from pathlib import Path

import click


SECRETS_STORE_DIR = 'secrets-store'


def list_secrets(dir_path=SECRETS_STORE_DIR):
    return [ 
        item.name 
        for item in Path(dir_path).iterdir() 
        if item.is_file()
    ]

def get_secret(secret, dir_path=SECRETS_STORE_DIR):
    path = Path(dir_path).joinpath(secret)
    with open(path, 'r') as fp:
        data = fp.read()
    return data

@click.command()
@click.option('--All', '-A', default=False, help='List all secrets', is_flag=True, required=False)
@click.option('--secret', '-s', type=str, help='Get specific secret')
def main(all: bool, secret: str):
    if all:
        print(list_secrets())
    if secret:
        try:
            print(get_secret(secret))
        except:
            print('Secret not found.')


if __name__ == '__main__':
    main()
