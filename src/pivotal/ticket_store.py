import requests
from src import config
from src.ticket import Ticket


def get_by_id(id):
    json_ticket = _fetch('/stories/{}'.format(id))
    return Ticket(
        id=id,
        title=json_ticket.get('name'),
        body=json_ticket.get('description'),
        url=json_ticket.get('url')
    )


def _fetch(path):
    response = requests.get(_build_url(path), headers=_build_headers())
    response.raise_for_status()
    return response.json()


def _build_url(path):
    return 'https://www.pivotaltracker.com/services/v5/projects/{project}{path}'.format(
        project=config.PIVOTAL_PROJECT_ID,
        path=path
    )


def _build_headers():
    return {'X-TrackerToken': config.PIVOTAL_API_KEY}
