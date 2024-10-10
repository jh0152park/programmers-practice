while 1:
    data = list(map(str, input().split()))
    if data[0] == "#":
        break

    if int(data[1]) > 17 or int(data[2]) >= 80:
        print(f"{data[0]} Senior")
    else:
        print(f"{data[0]} Junior")