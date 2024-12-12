import json
from sys import stdin


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = []
for line in stdin:
    numbers.append(int(line.strip()))
prime_dict = {}
for num in numbers:
    for candidate in range(2, num + 1):
        if is_prime(candidate):
            if num % candidate == 0:
                prime_dict.setdefault(candidate, []).append(num)
for key in prime_dict:
    prime_dict[key] = sorted(set(prime_dict[key]))
with open("result.json", "w") as outfile:
    json.dump(prime_dict, outfile, indent=4)