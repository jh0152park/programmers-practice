import sys


def convert_to_sec(times):
    return (times[0] * 3600) + (times[1] * 60) + times[2]


def compute_work_time(people):
    start = convert_to_sec(people[0:3])
    end = convert_to_sec(people[3:])
    time = end - start

    h = time // 3600
    m = time % 3600 // 60
    s = time % 3600 % 60

    sys.stdout.write(f"{h} {m} {s}\n")


for _ in range(3):
    worker = list(map(int, sys.stdin.readline().strip().split()))
    compute_work_time(worker)