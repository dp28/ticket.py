from unittest.mock import Mock, patch
from unittest import TestCase

from ticket.commands.start_ticket import start_ticket, NotFoundError
from ticket.ticket import Ticket
from ticket.pivotal import ticket_store
from ticket.git.branch import Branch
from ticket.git.repos import Repo


class StartTicketTest(TestCase):

    def test_missing_ticket_throws_an_exception(self):
        mock_ticket_store = Mock()
        mock_ticket_store.get_by_id.return_value = None
        with self.assertRaises(NotFoundError):
            start_ticket('id', mock_ticket_store, Mock(), Mock())

    @patch('ticket.git.branch_store.create_branch')
    def test_branch_is_created_with_ticket_branch_name(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock()
        mock_ticket.branch = Mock(name='something')
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store, Mock(), Mock())

        create_branch.assert_called_with(mock_ticket.branch)

    @patch('ticket.git.branch_store.create_branch')
    def test_ticket_is_started_if_was_unstarted(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock(ticket_store)
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store, Mock(), Mock())
        self.assertEqual(1, mock_ticket.start.call_count)
        mock_ticket_store.save.assert_called_with(mock_ticket)


    @patch('ticket.git.branch_store.create_branch')
    @patch('ticket.git.repos.get_current')
    def test_pull_request_is_created_from_new_ticket(self, get_current_repo, create_branch):
        mock_repo = Mock(Repo)
        get_current_repo.return_value = mock_repo
        mock_pull_factory = Mock()
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock(ticket_store)
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store, mock_pull_factory, Mock())
        mock_pull_factory.create_pull_request.assert_called_with(mock_ticket, mock_repo)

    @patch('ticket.git.branch_store.create_branch')
    def test_pull_request_is_added_to_ticket(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock(ticket_store)
        mock_ticket_store.get_by_id.return_value = mock_ticket
        mock_pull_factory = Mock()
        mock_pull = Mock()
        mock_pull_factory.create_pull_request.return_value = mock_pull

        start_ticket('id', mock_ticket_store, mock_pull_factory, Mock())
        mock_ticket.add_pull_request.assert_called_with(mock_pull)

    @patch('ticket.git.branch_store.create_branch')
    def test_pull_request_is_saved(self, create_branch):
        mock_pull = Mock()
        mock_pull_factory = Mock()
        mock_pull_factory.create_pull_request.return_value = mock_pull
        mock_pull_store = Mock()

        start_ticket('id', Mock(), mock_pull_factory, mock_pull_store)
        mock_pull_store.save.assert_called_with(mock_pull)


