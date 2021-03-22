import sys


def print_error(error_str):
    sys.stderr.write(error_str + '\n')
    exit(1)