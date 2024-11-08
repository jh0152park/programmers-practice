import sys

"""
총 m개의 계단
가만히 있으면 1초에 s계단 상승
걸어가면 1초에 g계단 상승

왼쪽에는 a명이 1초마다 에스컬레이터를 걸어가고
오른쪽에는 b명이 에스컬레이터에 설 수 있음

왼쪽줄에 l명이 서있고
오른쪽줄에 r명이 서있음
"""
m, s, g = map(int, sys.stdin.readline().strip().split())
a, b = map(float, sys.stdin.readline().strip().split())
l, r = map(int, sys.stdin.readline().strip().split())


l_wait = l / a
r_wait = r / b
r_time = (m / s) + r_wait
l_time = (m / g) + l_wait

if r_time < l_time:
    print("latmask")
else:
    print("friskus")