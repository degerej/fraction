from fraction import Fraction

# Include the fractions, does not have to be specific.

first = Fraction(1,4)
second = Fraction(1,6)

answer = first.add(second)
print(str(answer.num) + "/" + str(answer.denom))

answer = first.subtract(second)
print(str(answer.num) + "/" + str(answer.denom))
