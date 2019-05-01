"""
[想定課題]
N 種類のコインが1枚ずつあります。コインの金額は、それぞれ a[0], a[1], …, a[n-1] 円です。
これらのコインの中から何枚か選び、合計金額を X 円にする方法は存在するでしょうか。
存在すれば Yes, 存在しなければ No と出力せよ。
"""

def func(i, x, a):
    """description
    a[0], a[1], ... , a[n-1] のうち、最初の i 個(a[0], a[1], ... ,a[i-1]) から何個か
    選び、総和を x にできるかどうか判定する関数。
    
    使い方: func(選べる項の数, 目標とする総和, コインそれぞれの値段の配列)
    返り値: 総和を x にできれば True, できなければ False を返す
    """
    
    # ベースケースの処理
    # i = 0 のとき、x = 0 となっていれば True。なっていなければ False。
    if i == 0:
        if x == 0:
            return True
        else:
            return False
    
    # ベースケースにたどり着くまでの処理 (個数と番目がややこしいので注意)
    # 1. i個目、すなわち a[i-1] が選ばれていない場合。
    # 2. i個目、すなわち a[i-1] が選ばれている場合。
    # 3. 1, 2 どちらも True にならなければ False。
    if func(i-1, x, a):
        return True
    if func(i-1, x - a[i-1], a):
        return True
    return False


# Yes となるケース
# N = 4
# X = 14
# costs = [3, 2, 5, 6]


# No となるケース
N = 5
X = 19
costs = [9, 8, 3, 1, 3] 


ans = "No"
if func(N, X, costs):
    ans = "Yes"
print(ans)
