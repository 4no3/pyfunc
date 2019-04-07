from gcd_simple import gcd


def lcm_simple(num1, num2):
    return (num1 * num2) // gcd(num1, num2)


a = 6
b = 9
print(lcm_simple(a, b))