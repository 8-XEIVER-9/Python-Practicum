class Fraction:
    def __init__(self, *args):
        self.minus = False
        if len(args) == 2:
            self.num, self.denum = self.__divs(args[0], args[1])
        else:
            arr = list(map(int, args[0].split("/")))
            self.num, self.denum = self.__divs(arr[0], arr[1])
        if (self.denum * self.num) < 0:
            self.minus = True
        self.num = abs(self.num)
        self.denum = abs(self.denum)
    
    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def __divs(self, num, denum):
        div = self.__gcd(num, denum)
        return num // div, denum // div
    
    def numerator(self, *args):
        if len(args):
            if args[0] < 0:
                self.minus = not self.minus
            self.num = abs(args[0])
            self.num, self.denum = self.__divs(self.num, self.denum)
        else:
            return self.num
    
    def denominator(self, *args):
        if len(args):
            if args[0] < 0:
                self.minus = not self.minus
            self.denum = abs(args[0])
            self.num, self.denum = self.__divs(self.num, self.denum)
        else:
            return self.denum

    def __str__(self):
        if self.minus:
            return f"-{self.num}/{self.denum}"
        return f"{self.num}/{self.denum}"
    
    def __repr__(self):
        return f"Fraction('{self.__str__()}')"
    
    def __neg__(self):
        return Fraction(f"{'-' if not self.minus else ''}{self.num}/{self.denum}")
