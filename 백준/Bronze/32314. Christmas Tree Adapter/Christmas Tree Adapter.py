tree = int(input())
w, v = map(int, input().split())

if w // v >= tree:
    print("1")
else:
    print("0")