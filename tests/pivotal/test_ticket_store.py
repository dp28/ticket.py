import pytest
from unittest.mock import patch, Mock

from ticket.pivotal import ticket_store
from ticket import config
from ticket.ticket import Ticket


@patch('requests.get')
def test_fetches_from_pivotal_api(get):
    ticket_store.get_by_id('bla')
    assert get.call_args[0][0] == _story_url('bla')


@patch('requests.get')
def test_uses_correct_auth_header(get):
    config.PIVOTAL_API_KEY = 'api_key'
    ticket_store.get_by_id('bla')
    assert get.call_args[1]['headers']['X-TrackerToken'] == 'api_key'


@patch('requests.get')
def test_attempts_to_raise_error_from_request(get):
    response = Mock()
    response.json.return_value = {}
    get.return_value = response
    ticket_store.get_by_id('bla')
    assert response.raise_for_status.call_count == 1


@patch('requests.get')
def test_converts_json_response_into_ticket(get):
    response = Mock()
    response.json.return_value = {
        'id': 'bla',
        'url': 'http://a.b/c',
        'name': 'abc',
        'description': 'bla bla',
        'current_state': 'finished'
    }
    get.return_value = response
    ticket = ticket_store.get_by_id('bla')
    assert ticket.id == 'bla'
    assert ticket.title == 'abc'
    assert ticket.url == 'http://a.b/c'
    assert ticket.body == 'bla bla'
    assert ticket.state == 'finished'


@patch('requests.get')
def test_converts_unscheduled_into_unstarted(get):
    response = Mock()
    response.json.return_value = {
        'id': 'bla',
        'url': 'http://a.b/c',
        'name': 'abc',
        'description': 'bla bla',
        'current_state': 'unscheduled'
    }
    get.return_value = response
    ticket = ticket_store.get_by_id('bla')
    assert ticket.state == 'unstarted'


@patch('requests.put')
def test_save_puts_ticket_to_pivotal(put):
    ticket = Ticket(id='a', title='title', body='body', state='state', url='e')
    ticket_store.save(ticket)
    assert put.call_args[0][0] == _story_url('a')
    assert put.call_args[1]['data'] == {
        'name': 'title',
        'description': 'body',
        'current_state': 'state'
    }


def _story_url(id):
    return 'https://www.pivotaltracker.com/services/v5/projects/{project}/stories/{id}'.format(
        id=id,
        project=config.PIVOTAL_PROJECT_ID
    )
