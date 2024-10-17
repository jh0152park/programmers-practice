import sys

n = int(sys.stdin.readline().strip())
sys.stdout.write(chr(ord("가") + n - 1))