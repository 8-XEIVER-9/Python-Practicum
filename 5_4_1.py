from math import log, sin, cos, pi, e


def f(x):
    return log(x**(3 / 16), 32) + x**cos((pi * x) / (2 * e)) - sin(x / pi)**2


print(f(float(input())))