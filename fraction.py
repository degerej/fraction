# Joe Degere
# 11/15/19
# Fractions!

# Starting off with defining the class


class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.denom = denominator

        # This function helps with adding

    def add(self, second):
        answer = Fraction(0,1)
        answer.num = self.num * second.denom + second.num * self.denom
        answer.denom = self.denom * second.denom
        return answer

    # The next function helps with subtracting, only difference is the add symbol turns to subtraction.

    def subtract(self, second):
        answer = Fraction(0,1)
        answer.num = self.num * second.denom - second.num * self.denom
        answer.denom = self.denom * second.denom
        return answer
