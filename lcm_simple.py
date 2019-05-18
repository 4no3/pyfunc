from gcd_simple import gcd


def lcm_simple(num1, num2):
    return (num1 * num2) // gcd(num1, num2)


# 動作確認
a = 6
b = 9
print(lcm_simple(a, b))


lst = [6, 21, 12, 33]
lcm = 1
for a in lst:
    lcm = lcm_simple(lcm, a)
print(lcm)
