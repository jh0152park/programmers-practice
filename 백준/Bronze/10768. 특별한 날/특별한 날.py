m = int(input())
d = int(input())

if m == 2:
    if d == 18:
        print("Special")
    elif d < 18:
        print("Before")
    else:
        print("After")
else:
    if m > 2:
        print("After")
    else:
        print("Before")