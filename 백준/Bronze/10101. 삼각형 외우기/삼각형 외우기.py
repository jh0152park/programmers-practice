angles = []

for _ in range(3):
    angles.append(int(input()))

angles.sort()

if sum(angles) != 180:
    print("Error")
elif angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
    print("Equilateral")
elif angles[0] == angles[1] or angles[1] == angles[2]:
    print("Isosceles")
else:
    print("Scalene")