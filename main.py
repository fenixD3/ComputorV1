from argparse_custom_error import ThrowingArgumentParser, ArgumentParserError
import sys

from parser import Parser
from polynomial import Polynomial


def process(polynomial, verbose_mode, graphic_mode):
    parser = Parser(polynomial, verbose_mode)
    parser.parse()
    polynomial = Polynomial(parser.get_parsed_polynomial(), parser.get_variable_char(), graphic_mode, parser.is_verbose)
    polynomial.print_reduced_form()
    polynomial.solve()


if __name__ == '__main__':
    argParser = ThrowingArgumentParser(description='Computor Vision V1')
    argParser.add_argument('-v', '--verbose', action='store_true', dest='verbose_mode', help='Write information about full steps')
    argParser.add_argument('-g', '--graphic', action='store_true', dest='graphic_mode', help='Show a graphic of input polynomial')
    argParser.add_argument('polynomial', type=str, help='Input polynomial')
    try:
        args = argParser.parse_args()
    except ArgumentParserError:
        argParser.print_help()
        sys.exit(1)
    process(args.polynomial, args.verbose_mode, args.graphic_mode)
