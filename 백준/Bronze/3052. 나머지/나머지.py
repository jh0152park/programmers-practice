mod = {}
for _ in range(10):
    n = int(input())
    mod[n % 42] = 1

print(len(mod.keys()))