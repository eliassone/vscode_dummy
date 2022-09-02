#%%
from entries import helloapp

helloapp.main()

#%%
from entries import env

env.main()

#%%
from pathlib import Path

from entries import secrets as entry_secrets
from utils.path import path_context

with path_context(Path('..')):
    secrets_list = entry_secrets.list_secrets()
    for s in secrets_list:
        print(s)
        print(entry_secrets.get_secret(s))
        print()

