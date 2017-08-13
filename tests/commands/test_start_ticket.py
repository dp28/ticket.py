import pytest
from unittest.mock import Mock, patch
from unittest import TestCase

from ticket.commands.start_ticket import start_ticket, NotFoundError
from ticket.ticket import Ticket
from ticket.pivotal import ticket_store


class StartTicketTest(TestCase):

    def test_missing_ticket_throws_an_exception(self):
        mock_ticket_store = Mock()
        mock_ticket_store.get_by_id.return_value = None
        with self.assertRaises(NotFoundError):
            start_ticket('id', mock_ticket_store)

    @patch('ticket.git.branch_factory.create_branch')
    def test_branch_is_created_with_ticket_branch_name(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock()
        mock_ticket.branch_name = 'something'
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store)

        create_branch.assert_called_with('something')

    @patch('ticket.git.branch_factory.create_branch')
    def test_ticket_is_started_if_was_unstarted(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock(ticket_store)
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store)
        self.assertEqual(1, mock_ticket.start.call_count)
        mock_ticket_store.save.assert_called_with(mock_ticket)

