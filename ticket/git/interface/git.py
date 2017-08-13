from ticket.cli import command_runner


def run(subcommand):
    return command_runner.run('git ' + subcommand)
