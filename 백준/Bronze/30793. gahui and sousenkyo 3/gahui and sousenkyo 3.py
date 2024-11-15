import sys


px, rx = map(int, sys.stdin.readline().strip().split())
vx = px / rx

if vx < 0.2:
    print("weak")
elif 0.2 <= vx < 0.4:
    print("normal")
elif 0.4 <= vx < 0.6:
    print("strong")
else:
    print("very strong")