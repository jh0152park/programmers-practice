letters = [0] * 26

string = input().strip()
for c in string:
    letters[ord(c) - ord("a")] += 1

print(*letters)