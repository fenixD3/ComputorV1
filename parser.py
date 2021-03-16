class Parser:

    def __init__(self, polynomialBuffer, isVerbose, needGraphic):
        self.mPolynomialBuffer = polynomialBuffer
        self.mIsVerbose = isVerbose
        self.mNeedGraphic = needGraphic
        self.mParsedPolynomial = []

    def parse(self):
        print(self.mPolynomialBuffer, type(self.mPolynomialBuffer))
        print(self.mPolynomialBuffer[0], type(self.mPolynomialBuffer[0]))
        print(int(self.mPolynomialBuffer[0]), type(int(self.mPolynomialBuffer[0])))
        if self.mIsVerbose:
            print("Process parsing input polynomial")
