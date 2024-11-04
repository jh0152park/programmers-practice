import sys


match1 = list(map(int, sys.stdin.readline().strip().split()))
match2 = list(map(int, sys.stdin.readline().strip().split()))

if match1 == match2:
    print("Penalty")
elif match1[0] + match2[1] > match1[1] + match2[0]:
    print("Persepolis")
elif match1[0] + match2[1] < match1[1] + match2[0]:
    print("Esteghlal")
elif match1[1] > match2[1]:
    print("Esteghlal")
else:
    print("Persepolis")