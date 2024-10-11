sugar = 0
kg = int(input())


while kg >= 3:
    if kg % 5 == 0:
        sugar += kg // 5
        kg = 0
        break
    sugar += 1
    kg -= 3

if kg:
    print("-1")
else:
    print(sugar)