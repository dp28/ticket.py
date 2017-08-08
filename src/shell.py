from subprocess import check_output

def run(command):
    return check_output(command.split(' '), universal_newlines=True).rstrip('\n')
