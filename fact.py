# lru_cache を使った自作関数
from functools import lru_cache
# import sys
# sys.setrecursionlimit(500000)


@lru_cache(maxsize=None)
def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)
n = 20
print("Factorial is ", fact(n))


# 標準モジュールを利用した場合
import math


fact_num = math.factorial(n)
print("Factorial is ", fact_num)