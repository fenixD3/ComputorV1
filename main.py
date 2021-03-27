# coding=utf-8
import argparse
import sys

from parser import Parser
from polynomial import Polynomial


def process(polynomial, isVerbose, needGraphic):
    parser = Parser(polynomial, isVerbose, needGraphic)
    parser.parse()
    polynomial = Polynomial(parser.get_parsed_polynomial(), parser.get_variable_char(), parser.mNeedGraphic, parser.mIsVerbose)
    polynomial.print_reduced_form()
    polynomial.solve()

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
