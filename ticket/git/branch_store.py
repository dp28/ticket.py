from ticket.git.interface import git
from ticket.git.branch import Branch
from ticket.config import BRANCH_POINT
from ticket.cli.command_runner import CommandFailedError


def create_branch(branch):
    git.run('checkout ' + BRANCH_POINT)
    git.run('pull')
    try:
        git.run('checkout -b ' + branch.name)
    except CommandFailedError:
        pass # already exists

    return branch
