import sys


w1 = int(sys.stdin.readline().strip())
h1 = int(sys.stdin.readline().strip())
w2 = int(sys.stdin.readline().strip())
h2 = int(sys.stdin.readline().strip())

h = h1 + h2
if w1 == w2:
    w = w1 + 2    
    print(w * 2 + h + h)
elif w2 > w1:
    print(h + h + w1 + 2 + w2 + 2 + (w2 - w1))
else:
    print(h + h + w1 + 2 + w2 + 2 + (w1 - w2))