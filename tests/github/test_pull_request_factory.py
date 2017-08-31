import pytest
from unittest.mock import Mock

from ticket.github.pull_request import PullRequest
from ticket.git.repos import Repo
from ticket.ticket import Ticket
from ticket.github import pull_request_factory


def test_pull_request_is_created_with_ticket():
    mock_ticket = Mock(Ticket)
    request = pull_request_factory.create_pull_request(mock_ticket, Mock())
    assert request.ticket == mock_ticket



def test_pull_request_is_created_with_repo():
    mock_repo = Mock(Repo)
    request = pull_request_factory.create_pull_request(Mock(), mock_repo)
    assert request.repo == mock_repo
