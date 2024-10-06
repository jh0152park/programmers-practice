dices =  sorted(list(map(int, input().split())))

if dices[0] == dices[1] == dices[2]:
    print(dices[0] * 1000 + 10000)
elif (dices[0] == dices[1] or dices[1] == dices[2]) and dices[0] != dices[2]:
    print(dices[1] * 100 + 1000)
else:
    print(dices[2] * 100)