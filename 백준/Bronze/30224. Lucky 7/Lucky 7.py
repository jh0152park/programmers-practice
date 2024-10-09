num = input().strip()

if "7" not in num:
    if int(num) % 7:
        print("0")
    else:
        print("1")
else:
    if int(num) % 7:
        print("2")
    else:
        print("3")