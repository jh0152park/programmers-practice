import sys


s = sys.stdin.readline().strip()
s = s.replace("a", "4")
s = s.replace("e", "3")
s = s.replace("i", "1")
s = s.replace("o", "0")
s = s.replace("s", "5")

print(s)