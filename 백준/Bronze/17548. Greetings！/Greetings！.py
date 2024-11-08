import sys


hey = sys.stdin.readline().strip()
e = hey.count("e") * 2
print(f"h{'e' * e}y")