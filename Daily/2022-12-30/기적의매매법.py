"""
BNP vs TIMING

TIMING : 전량 매수 & 전량 매도
1. 3일 연속 상승 -> 무조건 하락
2. 3일 연속 하락 -> 무조건 상승
3. 빚 x
"""

cash = int(input())
price = list(map(int, input().split()))

# BNP : 자산

cash_BNP, stock_BNP = cash, 0
for p in price:
    stock_BNP += cash_BNP // p
    cash_BNP %= p
# print(stock_BNP * p + cash_BNP)

# MACHINE : 자산
cash_TIMING, stock_TIMING = cash,0
up_streak = 0
down_streak = 0
prev = None
for p in price:
    if prev and p > prev:
        up_streak += 1
        down_streak = 0
    elif prev and p < prev:
        up_streak = 0
        down_streak += 1
    elif prev and p == prev:  # TODO : 이게 맞나?
        up_streak = 0
        down_streak = 0

    if up_streak >= 3:  # 매도 타이밍
        cash_TIMING += stock_TIMING * p
        stock_TIMING = 0
    elif down_streak >= 3:  # 매수 타이밍
        stock_TIMING += cash_TIMING // p
        cash_TIMING %= p
    prev = p

# print(cash_TIMING + stock_TIMING * p)

if stock_BNP * p + cash_BNP > cash_TIMING + stock_TIMING * p:
    print("BNP")
elif stock_BNP * p + cash_BNP < cash_TIMING + stock_TIMING * p:
    print("TIMING")
else:
    print("SAMESAME")