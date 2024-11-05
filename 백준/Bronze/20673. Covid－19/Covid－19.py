import sys


covid = int(sys.stdin.readline().strip())
patient = int(sys.stdin.readline().strip())

if covid <= 50 and patient <= 10:
    print("White")
elif patient > 30:
    print("Red")
else:
    print("Yellow")