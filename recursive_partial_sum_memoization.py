"""
[想定課題]
N 種類のコインが1枚ずつあります。コインの金額は、それぞれ a[0], a[1], …, a[n-1] 円です。
これらのコインの中から何枚か選び、合計金額を X 円にする方法は存在するでしょうか。
存在すれば Yes, 存在しなければ No と出力せよ。
"""


def func(i, x, a, dp):
    """
    概要:
    a[0], a[1], ... , a[n-1] のうち、最初の i 個(a[0], a[1], ... ,a[i-1]) から何個か
    選び、総和を x にできるか否か判定する関数。メモ化に対応。
    
    使い方: func(選べるコインの枚数, 目標とする総和, コインそれぞれの値段の配列, memo)
    返り値: 総和を x にできれば True, できなければ False
    """
    
    # ベースケースの処理
    if i == 0:
        if x == 0:
            return True
        else:
            return False
    
    # メモを確認する
    if dp[i][x]:
        return dp[i][x]
    
    # ベースケースにたどり着くまでの処理
    # * i 個目の項 a[i-1] が選ばれずに、残りの i-1 枚からコインを選んで総和 x を達成する場合
    # * i 個目の項 a[i-1] が選ばれて、残りの i-1 枚からコインを選んで総和 x - a[i-1] を達成する場合
    if func(i-1, x, a, dp):
        dp[i][x] = True
        return dp[i][x]
    if func(i-1, x - a[i-1], a, dp):
        dp[i][x] = True
        return dp[i][x]
    
    # * 上記どちらも True にならなければ目標総和を達成できないので False。
    dp[i][x] = False
    return dp[i][x]


# ===== 動作確認 =====
# 入力例
# * Yes の場合
N = 4
X = 14
costs = [3, 2, 5, 6]


# * No の場合
# N = 5
# X = 19
# costs = [9, 8, 3, 1, 3] 


dp = [[-1 for _ in range(X + 1)] for _ in range(N + 1)]
ans = "No"
if func(N, X, costs, dp):
    ans = "Yes"
print(ans)
