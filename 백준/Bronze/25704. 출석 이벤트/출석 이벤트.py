import sys


coupon = int(sys.stdin.readline().strip())
price = int(sys.stdin.readline().strip())


prices = [price]
if coupon >= 5:
    prices.append(price - 500 if price - 500 > 0 else 0)
if coupon >= 10:
    prices.append(int(price * 0.9))
if coupon >= 15:
    prices.append(price - 2000 if price - 2000 > 0 else 0)
if coupon >= 20:
    prices.append(int(price * 0.75))


print(min(prices))