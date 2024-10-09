str = input().strip()
opposite = ""

for c in str:
    if c.islower():
        opposite += c.upper()
    else:
        opposite += c.lower()

print(opposite)