import sys


antenna = int(sys.stdin.readline().strip())
eyes = int(sys.stdin.readline().strip())


if antenna >= 3 and eyes <= 4:
    print("TroyMartian")
if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")