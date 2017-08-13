from src.cli import command_runner


def git(subcommand):
    return command_runner.run('git ' + subcommand)
