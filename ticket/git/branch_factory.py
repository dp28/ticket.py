from re import sub
from ticket.git.branch import Branch
from ticket.config import BRANCH_PART_SEPARATOR, BRANCH_ID_PREFIX


def create_branch_from_id_and_title(id, title):
    ref = BRANCH_ID_PREFIX + id + BRANCH_PART_SEPARATOR + _sanitize(title)
    return Branch(ref)


def _sanitize(title):
    no_symbols = sub(r'[^\w\s\-_]+', '', title)
    return sub(r'\s+', BRANCH_PART_SEPARATOR, no_symbols).lower()
