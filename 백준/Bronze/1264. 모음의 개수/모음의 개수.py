letters = ["a", "e", "i", "o", "u"]

while 1:
    cnt = 0
    str = input().strip().lower()
    if str == "#":  break
    
    for c in str:
        if c in letters: cnt += 1
    print(cnt)