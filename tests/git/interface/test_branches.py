import pytest
from unittest.mock import patch
from unittest import TestCase

from ticket.git.interface import branches


class BranchesTest(TestCase):

    @patch('ticket.cli.command_runner.run')
    def test_current_branch(self, run):
        run.return_value = 'master'
        branch = branches.get_current_branch()
        self.assertEqual(run.call_count, 1)
        self.assertEqual(branch, 'master')

    @patch('ticket.cli.command_runner.run')
    def test_local_branches(self, run):
        run.return_value = '\n'.join(['* master', '  test', '  dev'])
        local_branches = branches.get_local_branches()
        self.assertEqual(run.call_count, 1)
        self.assertEqual(local_branches, ['master', 'test', 'dev'])

    @patch('ticket.cli.command_runner.run')
    def test_remote_branches(self, run):
        run.return_value = '\n'.join([' origin/master', '  heroku/master', '  origin/dev'])
        local_branches = branches.get_local_branches()
        self.assertEqual(run.call_count, 1)
        self.assertEqual(local_branches, ['origin/master', 'heroku/master', 'origin/dev'])
