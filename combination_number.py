from operator import mul
from functools import reduce


def cmb1(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under
# test
# print(cmb1(10000000, 1000))


# slow
# from math import factorial


# def cmb2(n, r):
#     f1 = factorial(n)
#     f2 = factorial(n - r)
#     f3 = factorial(r)
#     return f1 // f2 // f3
# test
# print(cmb2(1000000, 1000))