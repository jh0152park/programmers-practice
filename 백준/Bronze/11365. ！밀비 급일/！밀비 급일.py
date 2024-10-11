while True:
    code = input().strip()
    if code == "END":
        break
    print(code[::-1])