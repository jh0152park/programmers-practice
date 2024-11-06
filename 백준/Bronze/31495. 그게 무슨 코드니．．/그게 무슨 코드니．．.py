import sys


string = sys.stdin.readline().strip()

if len(string) <= 2 or string == '""' or not (string[0] == '"' and string[-1] == '"'):
    print("CE")
else:
    print(string[1:-1])