from unittest import TestCase
from unittest.mock import Mock

from ticket.ticket import Ticket


class TicketTest(TestCase):

    def test_creation_sets_id(self):
        ticket = Ticket(id='some_id', title='a title', body='a body', url='a url')
        self.assertEqual('some_id', ticket.id)

    def test_creation_sets_title(self):
        ticket = Ticket(id='some_id', title='a title', body='a body', url='a url')
        self.assertEqual('a title', ticket.title)

    def test_creation_sets_body(self):
        ticket = Ticket(id='some_id', title='a title', body='a body', url='a url')
        self.assertEqual('a body', ticket.body)

    def test_creation_sets_url(self):
        ticket = Ticket(id='some_id', title='a title', body='a body', url='a url')
        self.assertEqual('a url', ticket.url)

    def test_save_changes_state_to_started_if_was_unstarted(self):
        ticket = Ticket(state='unstarted')
        ticket.start()
        self.assertEqual('started', ticket.state)

    def test_save_changes_state_to_started_if_was_rejected(self):
        ticket = Ticket(state='rejected')
        ticket.start()
        self.assertEqual('started', ticket.state)

    def test_save_does_not_change_state_finished(self):
        ticket = Ticket(state='finished')
        ticket.start()
        self.assertEqual('finished', ticket.state)

    def test_add_pull_request_puts_pull_request_url_in_body(self):
        ticket = Ticket(body=None)
        mock_pull = Mock(url='http://a.b.c')
        ticket.add_pull_request(mock_pull)
        self.assertEqual(ticket.body, '\n# Pull Requests\nhttp://a.b.c')

    def test_add_pull_request_appends_pull_request_url_to_body_if_body_exists(self):
        ticket = Ticket(body='Bla bla bla\nbla')
        mock_pull = Mock(url='http://a.b.c')
        ticket.add_pull_request(mock_pull)
        self.assertEqual(ticket.body, 'Bla bla bla\nbla\n# Pull Requests\nhttp://a.b.c')
