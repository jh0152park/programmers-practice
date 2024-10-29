import sys


limit = int(sys.stdin.readline().strip())
speed = int(sys.stdin.readline().strip())

fee = 0
if 1 <= speed - limit <= 20:
    fee = 100
elif 21 <= speed - limit <= 30:
    fee = 270
elif speed - limit >= 31:
    fee = 500

if not fee:
    print("Congratulations, you are within the speed limit!")
else:
    print(f"You are speeding and your fine is ${fee}.")