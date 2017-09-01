import pytest
from unittest.mock import Mock

from ticket.github.pull_request import PullRequest
from ticket.git.branch import Branch

from ticket import config


def test_pull_request_has_a_head_branch():
    branch = Branch('test')
    pull = PullRequest(Mock(branch=branch), Mock())
    assert pull.head_branch == branch


def test_pull_request_has_the_branch_point_as_its_base():
    pull = PullRequest(None, Mock())
    assert pull.base_branch == Branch(config.BRANCH_POINT)


def test_pull_request_has_a_title_taken_from_the_branch_ref():
    branch = Branch('PT123-test-this-works')
    pull = PullRequest(Mock(branch=branch), Mock())
    assert pull.title == 'Test this works'


def test_pull_request_title_removes_underscores():
    branch = Branch('PT123-test_this_works')
    pull = PullRequest(Mock(branch=branch), Mock())
    assert pull.title == 'Test this works'


def test_pull_request_title_does_not_require_ticket_ids():
    branch = Branch('test_this_works')
    pull = PullRequest(Mock(branch=branch), Mock())
    assert pull.title == 'Test this works'


def test_pull_request_has_a_body_including_a_link_to_the_passed_in_ticket():
    ticket = Mock(url='http://a.b.c/d')
    pull = PullRequest(ticket, Mock())
    assert 'Ticket: http://a.b.c/d' in pull.body
