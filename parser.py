import re
from helpers import print_error


class Parser:

    def __init__(self, polynomial, isVerbose, needGraphic):
        self.mPolynomial = polynomial
        self.mIsVerbose = isVerbose
        self.mNeedGraphic = needGraphic
        self.mParsedPolynomial = []

    def parse(self):
        if '=' not in self.mPolynomial:
            print_error("Symbol = isn't found in polynomial")

        if self.mIsVerbose:
            print("Splitting input at left and fight side")
        left_side, right_side = self.mPolynomial.split('=')
        left_side = left_side.split()
        right_side = right_side.split()
        if self.mIsVerbose:
            print("Process parsing input polynomial")

        for idx_token in enumerate(left_side):
            index = idx_token[0]
            token = idx_token[1]
            token_type = self.get_token_type(token)

        for idx_token in enumerate(right_side):
            pass

    def get_token_type(self, token):
        has_digit = re.search(r'\d+\.\d+|\d+', token)
        has_sign = re.search(r'[\+,-,*,/]', token)
        has_variable = re.search(r'x', token)
        has_degree = re.search(r'\^', token)
        if has_degree:
            degree = token[has_degree.start(0) + 1:has_degree.start(0) + 2]

