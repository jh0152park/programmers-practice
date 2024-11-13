import sys


message = sys.stdin.readline().strip()
password = []

i = 0
while i < len(message):
    password.append(message[i])
    i += ord(message[i]) - ord("A") + 1
    
print("".join(password))