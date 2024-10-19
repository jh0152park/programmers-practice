import sys
import math


n = int(sys.stdin.readline().strip())
for _ in range(n):
    quater = 25
    dime = 10
    nickel = 5
    penny = 1
    
    money = int(sys.stdin.readline().strip())
    
    q = int(money // quater)
    d = int(money % quater // dime)
    n = int(money % quater % dime // nickel)
    p = money % quater % dime % nickel // penny

    print(q, d, n, p)