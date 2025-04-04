class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.num, self.denum = args[0], args[1]
        else:
            self.num, self.denum = map(int, args[0].split("/"))
        self.__simplify()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __simplify(self):
        gcd = self.__gcd(self.num, self.denum)
        self.num //= gcd
        self.denum //= gcd
        if self.denum < 0:
            self.num = -self.num
            self.denum = abs(self.denum)

    def numerator(self, *args):
        if len(args):
            self.num = args[0]
            self.__simplify()
        return abs(self.num)

    def denominator(self, *args):
        if len(args):
            self.denum = args[0]
            self.__simplify()
        return abs(self.denum)

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"Fraction('{self.__str__()}')"

    def __neg__(self):
        return Fraction(-self.num, self.denum)

    def __add__(self, other):
        new_num = self.num * other.denum + other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __sub__(self, other):
        new_num = self.num * other.denum - other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __iadd__(self, other):
        self.num = self.num * other.denum + other.num * self.denum
        self.denum = self.denum * other.denum
        self.__simplify()
        return self

    def __isub__(self, other):
        self.num = self.num * other.denum - other.num * self.denum
        self.denum = self.denum * other.denum
        self.__simplify()
        return self