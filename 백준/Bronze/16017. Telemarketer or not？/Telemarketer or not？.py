import sys



numbers = []
for _ in range(4):
    numbers.append(int(sys.stdin.readline().strip()))

if numbers[0] >= 8 and numbers[3] >= 8 and numbers[1] == numbers[2]:
    print("ignore")
else:
    print("answer")