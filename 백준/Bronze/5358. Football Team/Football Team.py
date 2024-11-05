import sys


while True:
    name = sys.stdin.readline().strip()
    if not name:
        break

    name = name.replace("e", "_")
    name = name.replace("i", "e")
    name = name.replace("_", "i")
    
    name = name.replace("E", "_")
    name = name.replace("I", "E")
    name = name.replace("_", "I")
    print(name)
