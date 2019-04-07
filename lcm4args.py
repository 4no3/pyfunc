from operator import mul
from functools import reduce
from gcd4args import gcd4args


def lcm4args(args):
    mul_number = reduce(mul, args)
    gcd_number = gcd4args(args)
    return mul_number // gcd_number


list_numbers = [10, 45, 100]
print("LCM is ", lcm4args(list_numbers))
