time, alcohol = map(int, input().split())

if alcohol or not (12 <= time <= 16):
    print("280")
else:
    print("320")
