import sys


cables = []
k, n = map(int, sys.stdin.readline().strip().split())

for _ in range(k):
    cables.append(int(sys.stdin.readline().strip()))

cm = 0
start = 1
end = max(cables)

while start <= end:
    cable = 0
    length = (start + end) // 2

    for c in cables:
        cable += c // length

    if cable >= n:
        cm = max(cm, length)
        start = length + 1
    else:
        end = length - 1

sys.stdout.write(f"{cm}\n")