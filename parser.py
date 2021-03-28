import re
from helpers import print_error

MULTIPLE_CHAR = '*'
ADDITIONAL_CHAR = '+'
EXPONENT_CHAR = '^'


class Parser:

    def __init__(self, polynomial, verbose_mode):
        self.polynomial_str = polynomial
        self.is_verbose = verbose_mode
        self._parsed_polynomial = dict()
        self._sides_variable_letters = list()

    def parse(self):
        if '=' not in self.polynomial_str:
            print_error("Symbol = isn't found in polynomial")

        try:
            left_side, right_side = self.polynomial_str.split('=')
        except ValueError:
            print_error("Must be only one sign =")
        left_side = re.sub(r'\s+', '', left_side)
        right_side = re.sub(r'\s+', '', right_side)
        if self.is_verbose:
            print("Splitting input at left and right side with replacing spacing chars")
            print("\tLeft side: {}; Right side: {}".format(left_side, right_side))

        self.__parse_side(left_side, False)
        if right_side != '0':
            self.__parse_side(right_side, True)
        if self.is_verbose:
            print("Filled polynomial dictionary (index - degree, value - coefficient)")
            print('\t', self._parsed_polynomial, sep='')

    def __parse_side(self, polynomial_side, is_right):
        if polynomial_side[0] == '-':
            polynomial_side = '-' + polynomial_side[1:].replace('-', '+-')
        else:
            polynomial_side = polynomial_side.replace('-', '+-')
        if self.is_verbose:
            print("Change '-' sign to '+-' excluding starting")
            print("\t{} side: {}".format("Right" if is_right else "Left", polynomial_side))

        side_array = polynomial_side.split(ADDITIONAL_CHAR)
        if self.is_verbose:
            print("Split {} side to polynomial members in array".format("right" if is_right else "left"))
            print('\t', side_array, sep='')

        coefficients, degrees = self.__check_polynomial_side(side_array)
        if self.is_verbose:
            print("Split {} side's polynomial members to coefficients and degrees".format("right" if is_right else "left"))
            print('\tCoefficients: {}; Degrees: {}'.format(coefficients, degrees), sep='')
        if is_right:
            coefficients = list(map(lambda coefficient: -float(coefficient), coefficients))
        else:
            coefficients = list(map(float, coefficients))
        degrees = list(map(int, degrees))

        for degree in degrees:
            if self._parsed_polynomial.get(degree) is None:
                self._parsed_polynomial[degree] = coefficients[degree]
            else:
                self._parsed_polynomial[degree] += coefficients[degree]

    def __check_polynomial_side(self, side_array):
        for element in side_array:
            has_multiple = re.search(r'-\w*\.\w*\*|-\w*\*|\w*\*', element)
            if not has_multiple:
                print_error("There isn't multiplication operation")
            coefficient, var_with_degree = element.split(MULTIPLE_CHAR)
            try:
                float(coefficient)
            except ValueError:
                print_error("Coefficient isn't a number")
            has_exponent = re.search(r'\^', var_with_degree)
            if not has_exponent:
                print_error("There isn't exponent char")
            variable, degree = var_with_degree.split(EXPONENT_CHAR)
            if not variable.isalpha():
                print_error("Variable must be a letter")
            if not (degree.isnumeric() and int(degree) >= 0):
                print_error("Degree must be integer equal or greater 0")

        coefficients = [member.split(MULTIPLE_CHAR)[0] for member in side_array]
        variables = [member.split(MULTIPLE_CHAR)[1].split(EXPONENT_CHAR)[0].lower() for member in side_array]
        degrees = [member.split(MULTIPLE_CHAR)[1].split(EXPONENT_CHAR)[1] for member in side_array]

        for variable in variables[1:]:
            if variable != variables[0]:
                print_error("Variables must contain the same letters")
        self._sides_variable_letters.append(variables[0])
        if len(self._sides_variable_letters) == 2 and self._sides_variable_letters[0] != self._sides_variable_letters[1]:
            print_error("Variables letter in left and right side must be equaled")
        if not degrees == list(map(str, range(len(degrees)))):
            print_error("Degrees must increment from 0 to len(degrees) - 1")
        return coefficients, degrees

    def get_parsed_polynomial(self):
        return self._parsed_polynomial

    def get_variable_char(self):
        return self._sides_variable_letters[0]
