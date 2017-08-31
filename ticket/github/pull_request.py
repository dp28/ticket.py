from re import sub
from ticket import config
from ticket.git.branch import Branch


class PullRequest():

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
        return _humanize(self._get_head_branch_without_ticket_id())

    def _get_head_branch_without_ticket_id(self):
        branch_name = self.head_branch.name

        try:
            branch_prefix_end = branch_name.index(config.BRANCH_PART_SEPARATOR) + 1
            return branch_name[branch_prefix_end:]
        except ValueError:
            return branch_name


def _humanize(string):
    with_spaces = sub(r'[-_]', ' ', string)
    return with_spaces[0:1].upper() + with_spaces[1:]
