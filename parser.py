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

        self.__check_polynomial_side(side_array, is_right)

    def __check_polynomial_side(self, side_array, is_right):
        for element in side_array:
            global coefficient
            global degree
            has_multiple = re.search(r'-\w*\.\w*\*|-\w*\*|\w*\*', element)
            if has_multiple:
                coefficient, var_with_degree = element.split(MULTIPLE_CHAR)
                self.__check_coefficient(coefficient)
                degree = self.__check_variable_degree(var_with_degree)
            else:
                variable = re.search(r'[a-z|A-Z]', element)
                if variable:
                    var_with_degree = element[variable.start():]
                    coefficient = self.__check_coefficient(element[:variable.start()])
                    degree = self.__check_variable_degree(var_with_degree)
                else:
                    coefficient = element
                    self.__check_coefficient(coefficient)
                    degree = 0
            self.__fill_parsed_polynomial(int(degree), float(coefficient) if not is_right else -float(coefficient))
        self.__sort_parsed_polynomial()

    def __check_variable_degree(self, var_with_degree):
        if not (EXPONENT_CHAR in var_with_degree):
            variable = var_with_degree
            self.__check_variable(variable.lower())
            return '1'
        else:
            variable, member_degree = var_with_degree.split(EXPONENT_CHAR)
            self.__check_degree(member_degree)
            self.__check_variable(variable.lower())
            return member_degree

    def __check_coefficient(self, member_coefficient):
        if member_coefficient == '':
            return '1'
        try:
            float(member_coefficient)
        except ValueError:
            print_error("Coefficient isn't a number")
        return member_coefficient

    def __check_degree(self, member_degree):
        if not (member_degree.isnumeric() and int(member_degree) >= 0):
            print_error("Degree must be integer equal or greater 0")

    def __check_variable(self, variable):
        if not variable.isalpha():
            print_error("Variable must be a letter")
        if len(self._sides_variable_letters) == 0:
            self._sides_variable_letters.append(variable)
        if variable != self._sides_variable_letters[0]:
            print_error("Variables must contain the same letters")

    def __fill_parsed_polynomial(self, member_degree, member_coefficient):
        if self._parsed_polynomial.get(member_degree) is None:
            self._parsed_polynomial[member_degree] = member_coefficient
        else:
            self._parsed_polynomial[member_degree] += member_coefficient

    def __sort_parsed_polynomial(self):
        degrees = list(self._parsed_polynomial.keys())
        degrees.sort()
        coefficients = list()
        for degr in degrees:
            coefficients.append(self._parsed_polynomial[degr])
        self._parsed_polynomial.clear()
        for i in range(len(degrees)):
            self.__fill_parsed_polynomial(degrees[i], coefficients[i])

    def get_parsed_polynomial(self):
        return self._parsed_polynomial

    def get_variable_char(self):
        if len(self._sides_variable_letters) == 0:
            return 'x'
        return self._sides_variable_letters[0]
