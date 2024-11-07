import sys


t1, v1 = map(int, sys.stdin.readline().strip().split())
t2, v2 = map(int, sys.stdin.readline().strip().split())

if t2 < 0 and v2 >= 10:
    print("A storm warning for tomorrow!\nBe careful and stay home if possible!")
elif t2 < t1:
    print("MCHS warns! Low temperature\nis expected tomorrow.")
elif v2 > v1:
    print("MCHS warns! Strong wind\nis expected tomorrow.")
else:
    print("No message")