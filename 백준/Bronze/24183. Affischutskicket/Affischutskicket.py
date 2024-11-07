import sys


c4, a3, a4 = map(int, sys.stdin.readline().strip().split())
weights = [0.229 * 0.324, 0.297 * 0.420, 0.210 * 0.297]

weight = c4 * 2 * weights[0]
weight += a3 * 2 * weights[1]
weight += a4 * weights[2]

print("%.6f"%(weight))