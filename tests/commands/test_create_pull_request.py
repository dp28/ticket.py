from unittest.mock import Mock, patch
from unittest import TestCase

from ticket.commands.create_pull_request import create_pull_request
from ticket.ticket import Ticket
from ticket.pivotal import ticket_store
from ticket.git.branch import Branch
from ticket.git.repos import Repo


@patch('ticket.git.repos.get_current')
def test_pull_request_is_created_from_current_ticket(get_current_repo):
    mock_repo = Mock(Repo)
    get_current_repo.return_value = mock_repo
    mock_pull_factory = Mock()
    mock_ticket = Mock(Ticket)
    mock_ticket_store = Mock(ticket_store)
    mock_ticket_store.get_current.return_value = mock_ticket

    create_pull_request(mock_ticket_store, mock_pull_factory, Mock())
    mock_pull_factory.create_pull_request.assert_called_with(mock_ticket, mock_repo)


def test_pull_request_is_added_to_ticket():
    mock_ticket = Mock(Ticket)
    mock_ticket_store = Mock(ticket_store)
    mock_ticket_store.get_current.return_value = mock_ticket
    mock_pull_factory = Mock()
    mock_pull = Mock()
    mock_pull_factory.create_pull_request.return_value = mock_pull

    create_pull_request(mock_ticket_store, mock_pull_factory, Mock())
    mock_ticket.add_pull_request.assert_called_with(mock_pull)


def test_pull_request_is_saved():
    mock_pull = Mock()
    mock_pull_factory = Mock()
    mock_pull_factory.create_pull_request.return_value = mock_pull
    mock_pull_store = Mock()

    create_pull_request(Mock(), mock_pull_factory, mock_pull_store)
    mock_pull_store.save.assert_called_with(mock_pull)


def test_ticket_is_saved():
    mock_ticket = Mock(Ticket)
    mock_ticket_store = Mock(ticket_store)
    mock_ticket_store.get_current.return_value = mock_ticket

    create_pull_request(mock_ticket_store, Mock(), Mock())
    mock_ticket_store.save.assert_called_with(mock_ticket)


