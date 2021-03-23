import re
from helpers import print_error


class Parser:

    def __init__(self, polynomial, isVerbose, needGraphic):
        self.mPolynomial = polynomial
        self.mIsVerbose = isVerbose
        self.mNeedGraphic = needGraphic
        self.mParsedPolynomial = list()

    def parse(self):
        if '=' not in self.mPolynomial:
            print_error("Symbol = isn't found in polynomial")

        if self.mIsVerbose:
            print("Splitting input at left and fight side")
        left_side, right_side = self.mPolynomial.split('=')
        left_side = left_side.replace(' ', '')
        right_side = right_side.replace(' ', '')
        if self.mIsVerbose:
            print("Process parsing input polynomial")
            print("Change '-' sign to '+-' excluding starting")
        self.__parse_side(left_side, False)
        self.__parse_side(left_side, True)

    def __parse_side(self, polynomialSide, isRight):
        if polynomialSide[0] == '-':
            polynomialSide = '-' + polynomialSide[1:].replace('-', '+-')
        else:
            polynomialSide = polynomialSide.replace('-', '+-')
        side_array = polynomialSide.split('+')  # replace '+' to const var
        for element in side_array:
            self.__parse_polynomial_member(element)

    def __parse_polynomial_member(self, element):
        has_multiple = re.match(r'-\w*\.\w*\*|-\w*\*|\w*\*', element)
        if not has_multiple:
            print_error("There isn't multiplication operation")
        coefficient, var_with_degree = element.split('*')
        try:
            int(coefficient)
            float(coefficient)
        except ValueError:
            print_error("Coefficient isn't a number")
