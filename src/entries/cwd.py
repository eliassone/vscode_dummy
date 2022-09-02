import logging
from pathlib import Path

import click
import bunyan

from utils.path import path_context

_LOG = logging.getLogger(__name__)

def cwd():
    return Path.cwd()

@click.command()
@click.option('--context', '-c', type=str, help='', required=True)
def main(context: str):
    
    _LOG.info(f'PRE', extra={'cwd':cwd()})

    with path_context(Path(context)):
        _LOG.info(f'IN', extra={'cwd':cwd()})

    _LOG.info(f'POST', extra={'cwd':cwd()})

if __name__ == '__main__':
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = bunyan.BunyanFormatter()
    
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)
    
    main()