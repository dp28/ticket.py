import re
from ticket.config import BRANCH_PART_SEPARATOR, BRANCH_ID_PREFIX


REF_REGEX = (
    re.escape(BRANCH_ID_PREFIX) +
    r'(?P<ticket_id>\w+)' +
    re.escape(BRANCH_PART_SEPARATOR) +
    r'(?P<title>.*)'
)


class Branch():

    def __init__(self, ref):
        self.__ref = ref

    @property
    def ref(self):
        return self.__ref

    def __eq__(self, other_branch):
        return (isinstance(other_branch, Branch)
            and self.ref == other_branch.ref)

    @property
    def ticket_id(self):
        return self._get_ref_part('ticket_id')

    def human_readable(self):
        ref_without_id = self._get_ref_part('title') or self.ref
        with_spaces = re.sub(r'[-_]', ' ', ref_without_id)
        return with_spaces[0:1].upper() + with_spaces[1:]

    def _get_ref_part(self, part_name):
        match = re.search(REF_REGEX, self.ref)
        if match is None:
            return None
        else:
            return match.group(part_name)

