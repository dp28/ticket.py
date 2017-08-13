import pytest
from unittest.mock import Mock, patch
from unittest import TestCase

from src.commands.start_ticket import start_ticket, NotFoundError
from src.ticket import Ticket


class StartTicketTest(TestCase):

    def test_missing_ticket_throws_an_exception(self):
        mock_ticket_store = Mock()
        mock_ticket_store.get_by_id.return_value = None
        with self.assertRaises(NotFoundError):
            start_ticket('id', mock_ticket_store)

    @patch('src.git.branch_factory.create_branch')
    def test_branch_is_created_with_ticket_branch_name(self, create_branch):
        mock_ticket = Mock(Ticket)
        mock_ticket_store = Mock()
        mock_ticket.branch_name = 'something'
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store)

        create_branch.assert_called_with('something')

