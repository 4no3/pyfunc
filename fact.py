from functools import lru_cache
# import sys
# sys.setrecursionlimit(500000)


@lru_cache(maxsize=None)
def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)


n = 10
print("Factorial is ", fact(n))