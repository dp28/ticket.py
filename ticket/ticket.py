from re import sub


BRANCH_NAME_PREFIX = 'PT'
SEPARATOR = '-'

class Ticket():

    def __init__(self, id=None, title=None, body=None, url=None):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__url = url

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
    def branch_name(self):
        return BRANCH_NAME_PREFIX + self.id + SEPARATOR + self._build_sanitized_title()

    def _build_sanitized_title(self):
        no_symbols = sub(r'[^\w\s\-_]+', '', self.title)
        return sub(r'\s+', SEPARATOR, no_symbols).lower()
