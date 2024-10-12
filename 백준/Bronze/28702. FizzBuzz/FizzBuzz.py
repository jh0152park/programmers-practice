import sys

for i in range(3):
    data = sys.stdin.readline().strip()
    if data.isdigit():
        next = int(data) + (3 - i)
        if next % 3 == 0 and next % 5 == 0:
            sys.stdout.write("FizzBuzz")
        elif next % 3 == 0 and next % 5:
            sys.stdout.write("Fizz")
        elif next % 3 and next % 5 == 0:
            sys.stdout.write("Buzz")
        else:
            sys.stdout.write(f"{next}")
        break