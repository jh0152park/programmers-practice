import sys


plus = []
formula = sys.stdin.readline().strip()
for nums in formula.split("-"):
    if "+" not in nums:
        plus.append(int(nums))
    else:
        plus.append(sum(map(int, nums.split("+"))))

ret = plus[0]
for num in plus[1:]:
    ret -= num

print(ret)