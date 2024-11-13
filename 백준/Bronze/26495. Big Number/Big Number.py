import sys


def zero():
    print("0000")
    print("0  0")
    print("0  0")
    print("0  0")
    print("0000")

def one():
   print("   1")
   print("   1")
   print("   1")
   print("   1")
   print("   1")

def two():
    print("2222")
    print("   2")
    print("2222")
    print("2")
    print("2222")

def three():
    print("3333")
    print("   3")
    print("3333")
    print("   3")
    print("3333")

def four():
    print("4  4")
    print("4  4")
    print("4444")
    print("   4")
    print("   4")

def five():
    print("5555")
    print("5")
    print("5555")
    print("   5")
    print("5555")

def six():
    print("6666")
    print("6")
    print("6666")
    print("6  6")
    print("6666")

def seven():
    print("7777")
    print("   7")
    print("   7")
    print("   7")
    print("   7")

def eight():
    print("8888")
    print("8  8")
    print("8888")
    print("8  8")
    print("8888")

def nine():
    print("9999")
    print("9  9")
    print("9999")
    print("   9")
    print("   9")

def print_number(n):
    if int(n) == 0: zero()
    elif int(n) == 1: one()
    elif int(n) == 2: two()
    elif int(n) == 3: three()
    elif int(n) == 4: four()
    elif int(n) == 5: five()
    elif int(n) == 6: six()
    elif int(n) == 7: seven()
    elif int(n) == 8: eight()
    elif int(n) == 9: nine()


num = sys.stdin.readline().strip()

for n in num:
    print_number(n)
    print("")