class Rational:
    def __init__(self, n = 0, d = 1):
        from math import gcd
        self.__num = n//gcd(n,d)
        self.__den = d//gcd(n,d)

    def getNum(self):
        return self.__num
    def getDen(self):
        return self.__den

    def __add__(self,other):
        num = self.__num * other.getDen() + other.getNum() * self.__den
        den = self.__den * other.getDen()
        from math import gcd
        commFact = gcd(num,den)
        return Rational(num//commFact, den//commFact)
    def __sub__(self,other):
        return self + -1 * other

    def __mul__(self,other):
        num = 0
        den = 1
        if type(other) == type(Rational()):
            num = self.__num * other.getNum()
            den = self.__den * other.getDen()
        elif type(other) in [type(0), type(0.0)]:
            num = self.__num * other
            den = self.__den
        from math import gcd
        commFact = gcd(num,den)
        return Rational(num//commFact, den//commFact)
    def __truediv__(self,other):
        return (self.reciprocal() * other).reciprocal()

    def __repr__(self):
        if self.__den != 1:
            return str(self.__num) + '/' + str(self.__den)
        else:
            return str(self.__num)

    def reciprocal(self):
        return Rational(self.__den, self.__num)