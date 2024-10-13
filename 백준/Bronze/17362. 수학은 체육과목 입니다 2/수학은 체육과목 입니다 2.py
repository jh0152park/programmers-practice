def find_finger(n):
    finger_pattern = [1, 2, 3, 4, 5, 4, 3, 2]
    
    finger_index = (n - 1) % len(finger_pattern)
    
    return finger_pattern[finger_index]


n = int(input())
print(find_finger(n))
