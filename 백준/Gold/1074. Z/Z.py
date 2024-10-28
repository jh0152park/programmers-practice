import sys


def find_z_order(n, r, c):
    result = 0
    size = 2 ** n
    
    while size > 1:
        size //= 2
        
        # 각 사분면의 시작 번호와 크기 계산
        if r < size and c < size:
            # 1사분면 (왼쪽 위)
            pass
        elif r < size and c >= size:
            # 2사분면 (오른쪽 위)
            result += size * size
            c -= size
        elif r >= size and c < size:
            # 3사분면 (왼쪽 아래)
            result += 2 * size * size
            r -= size
        else:
            # 4사분면 (오른쪽 아래)
            result += 3 * size * size
            r -= size
            c -= size
            
    return result


n, r, c = map(int, sys.stdin.readline().strip().split())
print(find_z_order(n, r, c))