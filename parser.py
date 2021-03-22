import re
from helpers import print_error
from collections import namedtuple


token_properties = namedtuple('token_properties', 'has_digit, has_sign, has_variable, degree')


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
        print(left_side, right_side)
        if self.mIsVerbose:
            print("Process parsing input polynomial")
