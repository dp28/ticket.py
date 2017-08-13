import pytest
from unittest.mock import patch
from subprocess import CalledProcessError

from ticket.cli import command_runner
from ticket.cli.command_runner import CommandNotFoundError, CommandFailedError

@patch('subprocess.check_output')
def test_run_delegates_to_shell(check_output):
    command_runner.run('ls -l -a')
    check_output.assert_called_with(['ls', '-l', '-a'], universal_newlines=True)


@patch('subprocess.check_output', return_value='test\n')
def test_run_returns_command_output_without_trailing_newline(check_output):
    assert command_runner.run('ls') == 'test'


@patch('subprocess.check_output')
@patch('ticket.cli.output.show')
def test_run_prints_the_command_to_run(show, check_output):
    command_runner.run('ls')
    show.assert_called_with('ls')


@patch('subprocess.check_output', side_effect=OSError())
def test_run_raises_an_exception_if_the_command_does_not_exist(check_output):
    with pytest.raises(CommandNotFoundError):
        command_runner.run('asdfg')


@patch('subprocess.check_output', side_effect=CalledProcessError(2, ['git', 'completelyUnknownCommand']))
def test_run_raises_an_exception_if_the_command_fails(check_output):
    with pytest.raises(CommandFailedError):
        command_runner.run('git completelyUnknownCommand')

