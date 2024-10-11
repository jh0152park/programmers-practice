from itertools import combinations

n, k = map(int, input().split())
print(len(list(combinations([0] * n, k))))