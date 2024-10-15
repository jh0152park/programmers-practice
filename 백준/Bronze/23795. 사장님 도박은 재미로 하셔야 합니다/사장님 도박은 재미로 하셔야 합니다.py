import sys

money = 0
while True:
    m = int(sys.stdin.readline().strip())
    if m == -1:
        break
    money += m

sys.stdout.write(f"{money}")