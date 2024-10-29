import sys


depth = []
for _ in range(4):
    depth.append(int(sys.stdin.readline().strip()))

if depth[0] == depth[1] and depth[1] == depth[2] and depth[2] == depth[3]:
    print("Fish At Constant Depth")
elif depth[0] < depth[1] and depth[1] < depth[2] and depth[2] < depth[3]:
    print("Fish Rising")
elif depth[0] > depth[1] and depth[1] > depth[2] and depth[2] > depth[3]:
    print("Fish Diving")
else:
    print("No Fish")