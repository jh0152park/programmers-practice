import sys


n = int(sys.stdin.readline().strip())
id = sys.stdin.readline().strip()

id = id.replace("I", "i")
id = id.replace("l", "L")

print(id)