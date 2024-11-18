import sys

sequences = {
    "A": 0,
    "B": 1,
    "C": 2
}

nums = list(map(int, sys.stdin.readline().strip().split()))
sequence = sys.stdin.readline().strip()

nums.sort()
for seq in sequence:
    print(nums[sequences[seq]], end=" ")