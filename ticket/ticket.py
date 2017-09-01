from re import sub
from ticket.config import BRANCH_PART_SEPARATOR, BRANCH_ID_PREFIX
from ticket.git import branch_factory


class Ticket():

    def __init__(self, id=None, title=None, body=None, url=None, state='unstarted'):
        self.__id = id
        self.__title = title
        self.__body = body or ''
        self.__url = url
        self.__state = state

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

    @property
    def url(self):
        return self.__url

    @property
    def state(self):
        return self.__state

    @property
    def branch(self):
        return branch_factory.create_branch_from_id_and_title(self.id, self.title)

    def start(self):
        if self.state == 'unstarted' or self.state == 'rejected':
            self.__state = 'started'

    def add_pull_request(self, pull_request):
        self.__body += '\n# Pull Requests\n{}'.format(pull_request.url)
