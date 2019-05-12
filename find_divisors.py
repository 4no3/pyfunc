def find_divisors(n):
    lst_divisors = []
    last = int(n ** .5) + 1

    for a in range(1, last):
        if n % a == 0:
            lst_divisors.append(a)
            b = n // a
            if b != a:
                lst_divisors.append(b)
    
    lst_divisors.sort()

    return lst_divisors


# ===== 動作確認 =====
n = int(input())
lst_divisors = find_divisors(n)
print(lst_divisors)
