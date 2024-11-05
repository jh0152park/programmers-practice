import sys


for _ in range(15):
    pixel = list(map(str, sys.stdin.readline().strip().split()))
    if "w" in pixel:
        print("chunbae")
        break
    if "b" in pixel:
        print("nabi")
        break
    if "g" in pixel:
        print("yeongcheol")
        break