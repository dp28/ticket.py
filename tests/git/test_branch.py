import pytest

from ticket.git.branch import Branch


def test_branch_has_a_ref():
    branch = Branch('test')
    assert branch.ref == 'test'


def test_equality_is_done_by_ref():
    assert Branch('test') == Branch('test')
    assert Branch('test') != Branch('est')
