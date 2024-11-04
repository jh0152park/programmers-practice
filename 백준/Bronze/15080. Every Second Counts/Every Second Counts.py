import sys


def convert_to_sec(time):
    if time[0] == 0:
        time[0] = 24

    return (time[0] * 3600) + (time[1] * 60) + time[2]


ride = list(map(int, sys.stdin.readline().strip().split(" : ")))
off = list(map(int, sys.stdin.readline().strip().split(" : ")))


delta = convert_to_sec(off) - convert_to_sec(ride)
if delta < 0:
    delta += 86400
print(delta)