import sys


l = 0
k = 0
p = 0
for _ in range(3):
    s = sys.stdin.readline().strip()
    
    if s[0] == "l":
        l += 1
    elif s[0] == "k":
        k += 1
    elif s[0] == "p":
        p += 1

if l and k and p:
    print("GLOBAL")
else:
    print("PONIX")