letters = ["a", "e", "i", "o", "u"]

string = input().strip()
detect = 0
for c in string:
    if c in letters:
        detect += 1

print(detect)