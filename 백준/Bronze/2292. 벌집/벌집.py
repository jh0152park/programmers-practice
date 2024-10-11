import bisect

n = int(input())

psum = [1]
psum2 = [1]

i = 0
while True:
    psum.append((i + 1) * 6)
    psum2.append(psum2[-1] + psum[-1])
    if psum2[-1] >= 10 ** 9:
        break
    i += 1

print(bisect.bisect_left(psum2, n) + 1)