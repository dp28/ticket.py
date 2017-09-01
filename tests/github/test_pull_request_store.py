import pytest
from unittest.mock import Mock, patch, PropertyMock

from ticket.github.pull_request import PullRequest
from ticket.git.repos import Repo
from ticket.ticket import Ticket
from ticket.github import pull_request_store
from ticket import config

@patch('requests.post')
def test_posts_to_correct_url(post):
    mock_repo = Mock(Repo)
    mock_repo.name = 'a_repo'
    mock_pull = PullRequest(Mock(), mock_repo)
    config.GITHUB_REPO_OWNER = 'an_owner'
    pull_request_store.save(mock_pull)

    assert post.call_args[0][0] == 'https://api.github.com/repos/an_owner/a_repo/pulls'


@patch('requests.post')
def test_attempts_to_raise_error_from_request(post):
    response = Mock()
    response.json.return_value = {}
    post.return_value = response
    pull_request_store.save(Mock(PullRequest))
    assert response.raise_for_status.call_count == 1


@patch('requests.post')
def test_posts_correct_version_headers(post):
    pull_request_store.save(Mock(PullRequest))
    expected = 'application/vnd.github.v3+json'
    assert post.call_args[1]['headers']['Accept'] == expected


@patch('requests.post')
def test_posts_correct_auth_headers(post):
    config.GITHUB_API_KEY = 'test_token'
    pull_request_store.save(Mock(PullRequest))
    expected = 'token test_token'
    assert post.call_args[1]['headers']['Authorization'] == expected


@patch('requests.post')
def test_posts_correct_body(post):
    pull_request = Mock(PullRequest)
    pull_request.title = 'title'
    pull_request.head_branch.name = 'head'
    pull_request.base_branch.name = 'master'
    pull_request.body = 'a useful body'

    pull_request_store.save(pull_request)

    assert post.call_args[1]['data'] == dict(
        title='title',
        body='a useful body',
        head='head',
        base='master'
    )


@patch('requests.post')
def test_assigns_the_returned_url_to_the_pull_request(post):
    response = Mock()
    response.json.return_value = dict(url='http://a.b/c')
    post.return_value = response
    pull_request = Mock(PullRequest)
    pull_request_store.save(pull_request)

    assert pull_request.url == 'http://a.b/c'
