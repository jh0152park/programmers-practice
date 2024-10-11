data = [int(input()) for _ in range(5)]

kor = data[1] // data[3]
if data[1] % data[3]:
    kor += 1

math = data[2] // data[4]
if data[2] % data[4]:
    math += 1

print(data[0] - max(kor, math))