import subprocess
from src.cli import output
from src.errors import TicketError


def run(command):
    output.show(command)
    executable = command.split(' ')
    try:
        result = subprocess.check_output(executable, universal_newlines=True)
    except OSError:
        raise CommandNotFoundError(command)
    except subprocess.CalledProcessError as error:
        raise CommandFailedError(command, str(error))
    else:
        return result.rstrip('\n')


class CommandNotFoundError(TicketError):

    def __init__(self, command):
        super(CommandNotFoundError, self).__init__('"{}" is not a known command'.format(command))


class CommandFailedError(TicketError):

    def __init__(self, command, reason):
        super(CommandFailedError, self).__init__(
            '"{command}" failed: {reason}'.format(command=command, reason=reason)
        )


