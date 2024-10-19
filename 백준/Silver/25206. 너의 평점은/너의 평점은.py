import sys

grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

credit = 0.0
grade_sum = 0.0
for _ in range(20):
    name, score, grade = map(str, sys.stdin.readline().strip().split())
    
    if grade == "P":
        continue
        
    credit += float(score)
    grade_sum += grades[grade] * float(score)

if credit == 0.0:
    print("0.000000")
else:
    print("%.6f"%(grade_sum / credit))