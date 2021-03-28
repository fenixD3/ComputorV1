import matplotlib.pyplot as plt
import numpy as np

from helpers import absolut, float_to_int, sqrt


class Polynomial:

    def __init__(self, polynomial_dict, var_char, need_graph, is_verbose):
        self.polynomial = polynomial_dict
        self.variable_char = var_char
        self._need_graph = need_graph
        self._is_verbose = is_verbose

    def print_reduced_form(self):
        self.__remove_zero_coefficients()

        print('Reduced form: ', sep=' ', end='')
        dict_iteration = 0
        if len(self.polynomial) == 0:
            print('0 ', sep=' ', end='')
        for degree, coefficient in self.polynomial.items():
            dict_iteration += 1
            sign = '-' if coefficient < 0 else '+'
            coefficient = absolut(coefficient)
            coefficient = float_to_int(coefficient)
            if dict_iteration == 1 and sign == '-':
                print(sign, sep=' ', end='')
            elif degree > 0 and dict_iteration > 1:
                print(sign, ' ', sep='', end='')
            print('{} * {}^{} '.format(coefficient, self.variable_char, degree), sep=' ', end='')
        print('= 0')

    def __remove_zero_coefficients(self):
        removing_degree = []
        for degree, coefficient in self.polynomial.items():
            if coefficient == 0:
                removing_degree.append(degree)
        for degree in removing_degree:
            self.polynomial.pop(degree)

    def solve(self):
        degrees = list(self.polynomial.keys())
        if len(degrees) == 0:
            return print("Each real number is solution")
        polynomial_degree = degrees[len(degrees) - 1]
        print('Polynomial degree: {}'.format(polynomial_degree))
        if polynomial_degree > 2:
            return print("The polynomial degree is strictly greater than 2, I can't solve.")
        if polynomial_degree == 0:
            print("There isn't solution")
        elif polynomial_degree == 1:
            self.__solve_first_degree_function()
        elif polynomial_degree == 2:
            self.__solve_second_degree_function()
        if self._need_graph:
            self.__plot_graphic()

    def __solve_first_degree_function(self):
        """
            ax + b = 0
        """
        result = 0
        a = self.polynomial[1]
        b = self.polynomial.get(0, 0)
        if b != 0:
            result = -b / a
        print("The solution is:\n{:.2f}".format(result))

    def __solve_second_degree_function(self):
        """
            ax^2 + bx + c = 0
        """
        a = self.polynomial[2]
        b = self.polynomial.get(1, 0)
        c = self.polynomial.get(0, 0)
        discriminant = b ** 2 - 4. * a * c
        if self._is_verbose:
            print("Discriminant = {}".format(discriminant))

        if discriminant == 0:
            result = -b / (2 * a)
            print("Discriminant equal 0, the solution is:\n{:.2f}".format(result))
        elif discriminant > 0:
            result_1 = (-b + sqrt(discriminant)) / (2 * a)
            result_2 = (-b - sqrt(discriminant)) / (2 * a)
            print("Discriminant is strictly positive, the two solutions are:\n{:.2f}\n{:.2f}"
                  .format(result_1, result_2))
        else:
            discriminant = absolut(discriminant)
            integral = -b / (2 * a)
            imaginary = sqrt(discriminant) / (2 * a)
            print("Discriminant is negative, the two complex solutions are:\n{:.2f}+{:.2f}*{}\n{:.2f}-{:.2f}*{}"
                  .format(integral, imaginary, 'i', integral, imaginary, 'i'))

    def __plot_graphic(self):
        a = self.polynomial.get(2, 0)
        b = self.polynomial.get(1, 0)
        c = self.polynomial.get(0, 0)
        x = np.linspace(-10, 10, 25)
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)
        plt.grid(True)
        plt.show()
