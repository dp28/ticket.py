from src import shell


def get_current_branch():
    return _git('symbolic-ref --short HEAD')

def get_local_branches():
    return _parse_list(_git('branch'))

def get_remote_branches():
    return _parse_list(_git('branch --remote'))

def _git(subcommand):
    return shell.run('git ' + subcommand)

def _parse_list(list_string):
    print(list_string)
    return [
        item.strip('*').strip(' ')
        for item in list_string.split('\n')
        if len(item) > 0
    ]
