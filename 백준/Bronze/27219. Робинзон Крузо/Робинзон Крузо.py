day = int(input())

five = day // 5
day = day % 5

print(("V" * five) + ("I" * day))
