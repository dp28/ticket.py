from re import sub
from ticket import config
from ticket.git.branch import Branch


class PullRequest():

    url = None

    def __init__(self, ticket, repo):
        self.__ticket = ticket
        self.__repo = repo

    @property
    def ticket(self):
        return self.__ticket

    @property
    def repo(self):
        return self.__repo

    @property
    def head_branch(self):
        return self.ticket.branch

    @property
    def base_branch(self):
        return Branch(config.BRANCH_POINT)

    @property
    def body(self):
        return "Ticket: {url}".format(url=self.__ticket.url)

    @property
    def title(self):
        return self.head_branch.human_readable()
