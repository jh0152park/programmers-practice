t = int(input())
for _ in range(t):
    r, s = map(str, input().split())
    string = ""
    for c in s:
        string += c * int(r)
    print(string)