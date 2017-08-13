import sys

def show(text):
    print(text)


def show_error(text):
    sys.stderr.write(text + '\n')
