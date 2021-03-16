import argparse
import sys
import re

from parser import Parser


def process(polynomial, isVerbose, needGraphic):
    parser = Parser(re.split(r'\+', polynomial), isVerbose, needGraphic)
    parser.parse()

if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description='Computor Vision V1')
    argParser.add_argument('-v', '--verbose', action='store_true', dest='isVerbose', help='Write information about full steps')
    argParser.add_argument('-g', '--graphic', action='store_true', dest='needGraphic', help='Show a graphic of input polynomial')
    argParser.add_argument('polynomial', type=str, help='Input polynomial')
    try: # Возможно забить на обработку исключений
        args = argParser.parse_args()
    except BaseException:
        argParser.print_help()
        sys.exit(1)
    process(args.polynomial, args.isVerbose, args.needGraphic)
