import requests
from ticket import config
from ticket.ticket import Ticket


def get_by_id(id):
    json_ticket = _fetch(id)
    state = json_ticket.get('current_state', 'unstarted')
    if state == 'unscheduled':
        state = 'unstarted'

    return Ticket(
        id=id,
        title=json_ticket.get('name'),
        body=json_ticket.get('description'),
        url=json_ticket.get('url'),
        state=state
    )


def save(ticket):
    data = {
        'name': ticket.title,
        'description': ticket.body,
        'current_state': ticket.state
    }
    print('save')
    print(_put(ticket.id, data))


def _fetch(id):
    response = requests.get(_build_url(id), headers=_build_headers())
    response.raise_for_status()
    return response.json()


def _put(id, data):
    response = requests.put(_build_url(id), data=data, headers=_build_headers())
    response.raise_for_status()
    return response.json()


def _build_url(id):
    return 'https://www.pivotaltracker.com/services/v5/projects/{project}/stories/{id}'.format(
        project=config.PIVOTAL_PROJECT_ID,
        id=id
    )


def _build_headers():
    return {'X-TrackerToken': config.PIVOTAL_API_KEY}
