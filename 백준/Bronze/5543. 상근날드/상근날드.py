sodas = []
burgers = []

for _ in range(3):
    burgers.append(int(input()))

for _ in range(2):
    sodas.append(int(input()))

sodas.sort()
burgers.sort()

print(sodas[0] + burgers[0] - 50)