import re
from ticket.git.interface import git


def get_current_repo_name():
    remotes = git.run('remote -v')
    match = re.match(r'.*/(.+)\.git', remotes)
    return match.group(1)

