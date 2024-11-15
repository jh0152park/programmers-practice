import sys


s = sys.stdin.readline()
sys.stdout.write(s[0])
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        continue
    sys.stdout.write(s[i])