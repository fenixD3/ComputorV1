import re

class Parser:

    def __init__(self, polynomialBuffer, isVerbose, needGraphic):
        self.mPolynomialBuffer = polynomialBuffer
        self.mIsVerbose = isVerbose
        self.mNeedGraphic = needGraphic
        self.mParsedPolynomial = []

    def parse(self):
        print(self.mPolynomialBuffer)
        if self.mIsVerbose:
            print("Process parsing input polynomial")

        for idx_token in enumerate(self.mPolynomialBuffer):
            index = idx_token[0]
            token = idx_token[1]
            token_type = self.get_token_type(token)

    def get_token_type(self, token):
        has_digit = re.search(r'\d+', '55 55')
        if has_digit:
            print(has_digit.group(0))
        print(has_digit)
