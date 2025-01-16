import math

class Fraction:

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def add(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = (lcm / self.denominator) * self.numerator + (lcm / f.denominator) * f.numerator
        self.numerator = int(num)
        self.denominator = lcm

    def __add__(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = (lcm / self.denominator) * self.numerator + (lcm / f.denominator) * f.numerator
        return Fraction(int(num), lcm)
    
    def __sub__(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = (lcm / self.denominator) * self.numerator - (lcm / f.denominator) * f.numerator
        return Fraction(int(num), lcm)
    
    def __eq__(self, value):
        return self.numerator == value.numerator and self.denominator == value.denominator
    
    def __ne__(self, value):
        return self.numerator != value.numerator or self.denominator != value.den
    
    def __gt__(self, value):
        return (self.numerator / self.denominator) > (value.numerator / value.denominator)
    
    def __lt__(self, value):
        return (self.numerator / self.denominator) < (value.numerator / value.denominator)

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

f1 = Fraction(5, 10)
f2 = Fraction(2, 10)


result = f1 != f2
# f1.add(f1 - f2)
print(result)
print(result.numerator, result.denominator)

# print(f1)