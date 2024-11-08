import sys


lv, status = map(str, sys.stdin.readline().strip().split())
lv = int(lv)

if status == "miss":
    print("0")
elif status == "bad":
    print(lv * 200)
elif status == "cool":
    print(lv * 400)
elif status == "great":
    print(lv * 600)
else:
    print(lv * 1000)