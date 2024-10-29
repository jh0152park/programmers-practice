import sys


call_number = sys.stdin.readline().strip()
if call_number[0:3] == "555":
    print("YES")
else:
    print("NO")