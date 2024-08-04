def compute_correct_num(my_answer, answer):
    cycle = len(my_answer)
    correct = 0
    for idx, num in enumerate(answer):
        my_pick = my_answer[idx % cycle]
        if my_pick == num:
            correct += 1

    return correct
        

def solution(answers):
    answer = []
    supoja = [
        [1,2,3,4,5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    corrects = []
    for i in range(3):
        corrects.append(compute_correct_num(supoja[i], answers))
    
    max_correct = max(corrects)
    for i in range(3):
        if corrects[i] == max_correct:
            answer.append(i + 1)
            
    return answer
        