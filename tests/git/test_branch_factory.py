from unittest import TestCase
from unittest.mock import Mock

from ticket.git.branch_factory import create_branch_from_id_and_title
from ticket import config

config.BRANCH_PART_SEPARATOR = '-'
config.BRANCH_ID_PREFIX = 'PT'


def test_branch_ref_starts_with_prefix_and_id():
    branch = create_branch_from_id_and_title('1234', 'bla')
    name_start = branch.ref.split('-')[0]
    assert 'PT1234' == name_start


def test_branch_ref_ends_in_title():
    branch = create_branch_from_id_and_title('1234', 'bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla' == name_end


def test_branch_ref_replaces_spaces_in_title_with_hyphens():
    branch = create_branch_from_id_and_title('1234', 'bla bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla-bla' == name_end


def test_branch_ref_replaces_newlines_in_title_with_hyphens():
    branch = create_branch_from_id_and_title('1234', 'bla\nbla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla-bla' == name_end


def test_branch_ref_removes_symbols_in_title():
    branch = create_branch_from_id_and_title('1234', '[bla]$bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'blabla' == name_end


def test_branch_ref_keeps_undersores_in_title():
    branch = create_branch_from_id_and_title('1234', 'bla_bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla_bla' == name_end


def test_branch_ref_keeps_hyphens_in_title():
    branch = create_branch_from_id_and_title('1234', 'bla-bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla-bla' == name_end


def test_branch_ref_replaces_multiple_spaces_in_title_with_single_hyphens():
    branch = create_branch_from_id_and_title('1234', 'bla  bla')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla-bla' == name_end


def test_branch_ref_uses_downcased_title():
    branch = create_branch_from_id_and_title('1234', 'BlA  bLa')
    name_end = branch.ref.replace('PT1234-', '')
    assert 'bla-bla' == name_end
