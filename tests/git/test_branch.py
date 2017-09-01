import pytest
from ticket import config

from ticket.git.branch import Branch


def test_branch_has_a_ref():
    branch = Branch('test')
    assert branch.ref == 'test'


def test_equality_is_done_by_ref():
    assert Branch('test') == Branch('test')
    assert Branch('test') != Branch('est')


def test_ticket_id_is_none_if_not_in_ref():
    assert Branch('test').ticket_id is None


def test_ticket_id_is_returned_if_after_prefix_and_before_separator_in_ref():
    config.BRANCH_PART_SEPARATOR = '-'
    config.BRANCH_ID_PREFIX = 'PT'
    assert Branch('PT123-test').ticket_id == '123'


def test_human_readable_converts_hyphens_to_spaces():
    assert Branch('Test-branch').human_readable() == 'Test branch'


def test_human_readable_converts_underscores_to_spaces():
    assert Branch('Test_branch').human_readable() == 'Test branch'


def test_human_readable_capitalises_first_letter():
    assert Branch('test').human_readable() == 'Test'


def test_human_readable_does_not_include_ticket_id_or_prefix():
    config.BRANCH_PART_SEPARATOR = '-'
    config.BRANCH_ID_PREFIX = 'PT'
    assert Branch('PT123-test').human_readable() == 'Test'
