import sys


"""
입력
입력 첫 번째 줄은 확인할 고객의 수를 나타내는 양의 정수 n이며, 이후 각 n개의 줄에는 두 개의 정수를 제공합니다.
첫 번째 정수 c(1 ≤ c ≤ 100)는 고객이 구매한 품목의 수이고, 두 번째 정수 p(3 ≤ p ≤ 50)는 하나의 품목에 대한 가격입니다.

출력
각 고객에 대해 총 두 줄을 출력합니다.
첫 번째 줄에는 두 개의 입력 값을 공백으로 구분하여 출력, 두 번째 줄에는 고객의 총 비용을 출력합니다.
어떤 출력 줄에도 선행하거나 후행하는 공백이 없어야 합니다.
"""

n = int(sys.stdin.readline().strip())
for _ in range(n):
    c, p = map(int, sys.stdin.readline().strip().split())
    print(c, p)
    print((c * p) - ((c - 1) * 2))