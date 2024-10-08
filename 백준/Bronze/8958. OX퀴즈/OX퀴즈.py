def compute_score(answer):
    score = 0
    total_score = 0

    for ans in answer:
        if ans == "O":
            score += 1
        else:
            score = 0
        total_score += score

    return total_score


n = int(input())

for _ in range(n):
    answer = input().strip()
    print(compute_score(answer))