def much_digits(num):
    even = 0
    odd = 0
    for chr in num:
        if int(chr) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd:
        return "eq"
    if even > odd:
        return "even"
    if even < odd:
        return "odd"


numbers = input()
even = open(input(), "w", encoding="UTF-8")
odd = open(input(), "w", encoding="UTF-8")
eq = open(input(), "w", encoding="UTF-8")

with open(numbers, "r", encoding="UTF-8") as data:
    lines = data.readlines()
    for line in lines:
        evens = []
        odds = []
        eqs = []
        for num in line.split():
            match much_digits(num):
                case "eq":
                    eqs.append(num)
                case "even":
                    evens.append(num)
                case "odd":
                    odds.append(num)
        ans_ev = " ".join(evens) + "\n"
        ans_od = " ".join(odds) + "\n"
        ans_eq = " ".join(eqs) + "\n"
        even.write(ans_ev)
        odd.write(ans_od)
        eq.write(ans_eq)
even.close()
eq.close()
odd.close()