import sys

n, need = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

trees.sort()
start = 0
end = trees[-1]

h = float("-inf")
while start <= end:
    tree_sum = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            tree_sum += tree - mid

    if tree_sum >= need:
        h = max(h, mid)
        start = mid + 1
    else:
        end = mid - 1

print(h)