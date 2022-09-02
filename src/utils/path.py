import os, logging
from contextlib import contextmanager
from pathlib import Path

_LOG = logging.getLogger(__name__)

@contextmanager
def path_context(target_dir: Path):
    origin = Path().absolute()
    target = target_dir.absolute()
    _extra = {'origin': origin, 'target': target}
    try:
        os.chdir(target)
        _extra['cwd'] = Path.cwd().absolute()
        _LOG.warning('Directory path changed', extra={'data': _extra})
        yield
    finally:
        os.chdir(origin)
        _extra['cwd'] = Path.cwd().absolute()
        _LOG.warning('Directory path restored', extra={'data': _extra})