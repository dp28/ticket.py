import pytest
from unittest.mock import patch

from ticket.git.repos import Repo, get_current


def test_repo_has_a_name():
    repo = Repo('test')
    assert repo.name == 'test'


def test_repo_equality_depends_on_name():
    assert Repo('test') == Repo('test')


@patch('ticket.git.interface.repos.get_current_repo_name')
def test_get_current_returns_current_git_repo(get_current_repo):
    get_current_repo.return_value = 'test'
    assert get_current() == Repo('test')
