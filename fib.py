from functools import lru_cache
# import sys
# sys.setrecursionlimit(500000)


@lru_cache(maxsize=None)
def fib(number):
    if number < 2:
        return number
    return fib(number - 1) + fib(number - 2)


n = 10
print("Fibonacci is ", fib(n))