import pytest
import os
from unittest.mock import patch

from ticket.config_loader import fetch, ConfigValueMissingException
from ticket import config_loader

@patch('os.getenv', return_value='env')
def test_fetch_tries_environment_variables_prefixed_with_ticket(getenv):
    assert fetch('A') == 'env'
    getenv.assert_called_with('TICKET_A')


@patch('json.load', return_value={'B': 'json'})
@patch('builtins.open', create=True)
def test_fetch_tries_home_dir_config_file(open, load):
    config_loader.CUSTOM_CONFIG_PATH = '/home/user/.ticket.json'
    assert fetch('B') == 'json'
    open.assert_called_with('/home/user/.ticket.json')


@patch('builtins.open', create=True, side_effect=FileNotFoundError())
def test_does_not_require_config_file_to_exist(open):
    assert fetch('B') == None


@patch('builtins.open', create=True, side_effect=FileNotFoundError())
def test_uses_the_default_if_no_value_is_found(open):
    assert fetch('B', default='x') == 'x'


@patch('builtins.open', create=True, side_effect=FileNotFoundError())
def test_returns_none_if_no_value_or_default_is_found_and_required_is_false(open):
    assert fetch('B') == None


@patch('builtins.open', create=True, side_effect=FileNotFoundError())
def test_raises_if_no_value_or_default_is_found_and_required_is_true(open):
    with pytest.raises(ConfigValueMissingException):
        fetch('B', required=True)

