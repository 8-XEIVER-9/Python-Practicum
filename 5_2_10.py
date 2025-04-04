class Fraction:
    def __init__(self, *args):
        self.denum = 1
        if isinstance(args[0], str):
            splits = args[0].split('/')
            if len(splits) == 1:
                self.num = int(args[0])
            else:
                self.num, self.denum = [int(c) for c in splits]
        elif len(args) == 1 and isinstance(args[0], int):
            self.num = args[0]
        else:
            self.num = args[0]
            self.denum = args[1]
        self.__simplify()

    def _check_other(self, other):
        if isinstance(other, int):
            return Fraction(other, 1)
        return other
    
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
        other = self._check_other(other)
        new_num = self.num * other.denum + other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __sub__(self, other):
        other = self._check_other(other)
        new_num = self.num * other.denum - other.num * self.denum
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __iadd__(self, other):
        other = self._check_other(other)
        self.num = self.num * other.denum + other.num * self.denum
        self.denum = self.denum * other.denum
        self.__simplify()
        return self

    def __isub__(self, other):
        other = self._check_other(other)
        self.num = self.num * other.denum - other.num * self.denum
        self.denum = self.denum * other.denum
        self.__simplify()
        return self
    
    def __mul__(self, other):
        common_denominator = self.denum * other.denum
        new = Fraction(1, 1)
        new.num = self.num * other.num
        new.denum = common_denominator
        new.__simplify()
        return new

    def __truediv__(self, other):
        other = self._check_other(other)  # Используем _check_other
        new = Fraction(self.num, self.denum)
        new.__simplify()
        return new.__mul__(other.reverse())

    def __imul__(self, other):
        common_denominator = self.denum * other.denum
        self.num = self.num * other.num
        self.denum = common_denominator
        self.__simplify()
        return self

    def __itruediv__(self, other):
        other = self._check_other(other)
        return self.__imul__(other.reverse())
    
    def reverse(self):
        return Fraction(self.denum, self.num)
    
    def __gt__(self, other):
        other = self._check_other(other)
        return self.num * other.denum > other.num * self.denum

    def __lt__(self, other):
        other = self._check_other(other)
        return self.num * other.denum < other.num * self.denum

    def __ge__(self, other):
        other = self._check_other(other)
        return self.num * other.denum >= other.num * self.denum

    def __le__(self, other):
        other = self._check_other(other)
        return self.num * other.denum <= other.num * self.denum

    def __eq__(self, other):
        other = self._check_other(other)
        return self.num * other.denum == other.num * self.denum

    def __ne__(self, other):
        other = self._check_other(other)
        return self.num * other.denum != other.num * self.denum
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __rsub__(self, other):
        return -self.__sub__(other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __rtruediv__(self, other):
        other = self._check_other(other)  # Преобразуем other в Fraction
        return other.__truediv__(self)    # Выполняем деление
    
    def __rgt__(self, other):
        return self.__gt__(other)
    
    def __rlt__(self, other):
        return self.__lt__(other)
    
    def __rge__(self, other):
        return self.__ge__(other)
    
    def __rle__(self, other):
        return self.__le__(other)
    
    def __req__(self, other):
        return self.__eq__(other)
    
    def __rne__(self, other):
        return self.__ne__(other)