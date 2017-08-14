from unittest.mock import patch

from ticket.git.interface import repos


@patch('ticket.cli.command_runner.run')
def test_current_repo(run):
    run.return_value = 'origin  git@github.com:dp28/test.git (fetch)\norigin  git@github.com:dp28/test.git (push)'
    repo_name = repos.get_current_repo_name()
    assert run.call_count == 1
    assert repo_name == 'test'
