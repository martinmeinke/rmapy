from pathlib import Path
from yaml import BaseLoader
from yaml import load as yml_load
from yaml import dump as yml_dump
from typing import Dict


def config_file_path(token_file: str) -> Path:
    """Provide Path to config file"""

    if token_file is None:
        return Path.joinpath(Path.home(), ".rmapi")
    else:
        return Path(token_file)


def load(token_file: str) -> dict:
    """Load the .rmapy config file"""

    token_file = config_file_path(token_file)
    config: Dict[str, str] = {}
    if Path.exists(token_file):
        with open(token_file, 'r') as config_file:
            config = dict(yml_load(config_file.read(), Loader=BaseLoader))

    return config


def dump(config: dict, token_file: str) -> None:
    """Dump config to the .rmapy config file

    Args:
        config: A dict containing data to dump to the .rmapi
            config file.
    """

    token_file = config_file_path(token_file)

    with open(token_file, 'w') as config_file:
        config_file.write(yml_dump(config))
