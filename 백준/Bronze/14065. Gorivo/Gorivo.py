import sys


ratio = float(sys.stdin.readline().strip())
liters_per_100km = (3.785411784 / (ratio * 1.609344)) * 100
print(liters_per_100km)