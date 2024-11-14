import sys


heart = [
" @@@   @@@  ",
"@   @ @   @ ",
"@    @    @ ",
"@         @ ",
" @       @  ",
"  @     @   ",
"   @   @    ",
"    @ @     ",
"     @      ",
]

n = int(sys.stdin.readline().strip())

for h in heart:
    for _ in range(n):
        print(h, end="")
    print("")