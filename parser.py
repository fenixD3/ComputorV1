import re
from helpers import print_error


class Parser:

    def __init__(self, polynomial, isVerbose, needGraphic):
        self.mPolynomial = polynomial
        self.mIsVerbose = isVerbose
        self.mNeedGraphic = needGraphic
        self._parsed_polynomial = dict()
        self._sides_variable_letters = list()

    def parse(self):
        if '=' not in self.mPolynomial:
            print_error("Symbol = isn't found in polynomial")

        if self.mIsVerbose:
            print("Splitting input at left and fight side")
        try:
            left_side, right_side = self.mPolynomial.split('=')
        except ValueError:
            print_error("Must be only one sign =")
        left_side = left_side.replace(' ', '')
        right_side = right_side.replace(' ', '')

        if self.mIsVerbose:
            print("Process parsing input polynomial")
            print("Change '-' sign to '+-' excluding starting")
        self.__parse_side(left_side, False)
        if right_side != '0':
            self.__parse_side(right_side, True)

    def __parse_side(self, polynomial_side, isRight):
        if polynomial_side[0] == '-':
            polynomial_side = '-' + polynomial_side[1:].replace('-', '+-')
        else:
            polynomial_side = polynomial_side.replace('-', '+-')
        side_array = polynomial_side.split('+')  # replace '+' to const var
        coefficients, degrees = self.__check_polynomial_side(side_array)
        if isRight:
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
        if self.mIsVerbose:
            print("Checking polynomial side for right notation")

        for element in side_array:
            has_multiple = re.search(r'-\w*\.\w*\*|-\w*\*|\w*\*', element)
            if not has_multiple:
                print_error("There isn't multiplication operation")
            coefficient, var_with_degree = element.split('*')
            try:
                float(coefficient)
            except ValueError:
                print_error("Coefficient isn't a number")
            has_exponent = re.search(r'\^', var_with_degree)
            if not has_exponent:
                print_error("There isn't exponent char")
            variable, degree = var_with_degree.split('^')
            if not variable.isalpha():
                print_error("Variable must be a letter")
            if not (degree.isnumeric() and int(degree) >= 0):
                print_error("Variable must be a letter")

        coefficients = [member.split('*')[0] for member in side_array]
        variables = [member.split('*')[1].split('^')[0].lower() for member in side_array]
        degrees = [member.split('*')[1].split('^')[1] for member in side_array]

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
