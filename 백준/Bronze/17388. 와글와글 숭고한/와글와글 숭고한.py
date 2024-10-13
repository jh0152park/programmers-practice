import sys


invite = list(map(int, sys.stdin.readline().strip().split()))

if sum(invite) >= 100:
    sys.stdout.write("OK\n")
else:
    idx = invite.index(min(invite))
    name = ""
    if idx == 0:
        name = "Soongsil"
    elif idx == 1:
        name = "Korea"
    else:
        name = "Hanyang"
    sys.stdout.write(f"{name}\n")
        