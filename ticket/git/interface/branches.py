from ticket.git.interface import git


def get_current_branch():
    return git.run('symbolic-ref --short HEAD')


def get_local_branches():
    return _parse_list(git.run('branch'))


def get_remote_branches():
    return _parse_list(git.run('branch --remote'))


def _parse_list(list_string):
    print(list_string)
    return [
        item.strip('*').strip(' ')
        for item in list_string.split('\n')
        if len(item) > 0
    ]
