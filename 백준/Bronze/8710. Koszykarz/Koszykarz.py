import sys


tall, target, incress = map(int, sys.stdin.readline().strip().split())

hit = 0
while True:
    if tall >= target:
        break
    hit += 1
    tall += incress

print(hit)