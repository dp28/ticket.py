import pytest

from ticket.git.branch import Branch


def test_branch_has_a_name():
    branch = Branch('test')
    assert branch.name == 'test'


def test_equality_is_done_by_name():
    assert Branch('test') == Branch('test')
    assert Branch('test') != Branch('est')
