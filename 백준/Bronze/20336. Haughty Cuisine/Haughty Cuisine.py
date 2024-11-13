import sys


"""
입력

- 한 줄에 세트 메뉴의 수를 나타내는 하나의 정수 1 <= n <= 100이 주어집니다.

- n개의 각 줄에 세트 메뉴가 주어집니다. 각 줄에는 하나의 정수 1 <= d <= 42와, 그 세트를 구성하는 d개의 음식이 이어져 주어집니다. 

각 음식은 최대 20 개의 라틴 문자 소문자로 이루어져 있습니다.

출력

하나의 줄에 당신이 추천하는 세트 메뉴의 음식 수 m을 출력하고, 이어 m개의 줄에 당신이 추천하는 세트 메뉴의 음식을 출력합니다.

가능한 답이 여러 개라면, 아무 거나 출력하면 됩니다. 
"""

n = int(sys.stdin.readline().strip())

m = 0
menus = []
for _ in range(n):
    menu = sys.stdin.readline().strip().split()
    if int(menu[0]) > m:
        m = int(menu[0])
        menus = menu[1:]

print(m)
for menu in menus:
    print(menu)