from functools import reduce
from math import gcd        # Python3.5 以降
# from fractions import gcd   # Python3.4 以前


def gcd4args(args):
    return reduce(gcd, args)


list_num = [90, 81, 135]
print("GCD is ", gcd4args(list_num))
