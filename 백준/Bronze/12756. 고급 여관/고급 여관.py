import sys


atk_a, hp_a = map(int, sys.stdin.readline().strip().split())
atk_b, hp_b = map(int, sys.stdin.readline().strip().split())


dead_a = hp_a // atk_b + 1 if hp_a % atk_b else hp_a // atk_b
dead_b = hp_b // atk_a + 1 if hp_b % atk_a else hp_b // atk_a


if dead_a > dead_b:
    print("PLAYER A")
elif dead_a < dead_b:
    print("PLAYER B")
else:
    print("DRAW")