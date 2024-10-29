import sys


chicken, beef, pasta = map(int, sys.stdin.readline().strip().split())
c, b, p = map(int, sys.stdin.readline().strip().split())

missfire = 0

if c > chicken:
    missfire += c - chicken
if b > beef:
    missfire += b - beef
if p > pasta:
    missfire += p - pasta

print(missfire)