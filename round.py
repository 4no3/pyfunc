# 正確な四捨五入
from decimal import Decimal, ROUND_HALF_UP


num = 123.456
digit = 0.1
round_num = Decimal(str(num)).quantize(Decimal(str(digit)), rounding=ROUND_HALF_UP)
print(round_num)


# 自作の四捨五入関数
import math


def my_round(num, digit):
    p = 10 ** digit
    s = math.copysign(1, num)
    return (s * num * p * 2 + 1) // 2 / p * s
num = -123.456
print(my_round(num, 1))