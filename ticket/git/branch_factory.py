from ticket.git.interface import git
from ticket.git.branch import Branch
from ticket.config import BRANCH_POINT


def create_branch(branch_name):
    git.run('checkout ' + BRANCH_POINT)
    git.run('pull')
    git.run('checkout -b ' + branch_name)
    return Branch(branch_name)
