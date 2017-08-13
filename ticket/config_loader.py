import os
import json
from ticket.errors import TicketError


CUSTOM_CONFIG_PATH = os.path.expanduser('~/.ticket.json')


def fetch(key, default=None, required=False):
    env_var = os.getenv('TICKET_{}'.format(key))
    if env_var is not None:
        return env_var

    config_val = _fetch_from_custom_config(key)
    if config_val is not None:
        return config_val

    if required:
        raise ConfigValueMissingException(key)

    return default


def _fetch_from_custom_config(key):
    try:
        with open(CUSTOM_CONFIG_PATH) as json_content:
            custom_config = json.load(json_content)
            return custom_config.get(key)

    except FileNotFoundError:
        return None


class ConfigValueMissingException(TicketError):

    def __init__(self, key):
        super(ConfigValueMissingException, self).__init__("""
'{}' is a required value. Either add it to ~/.ticket.json or export it as an
environment variable""".format(key)
        )
