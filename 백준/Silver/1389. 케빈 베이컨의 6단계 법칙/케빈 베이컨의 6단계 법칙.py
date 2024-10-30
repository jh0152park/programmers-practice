import sys
input = sys.stdin.readline

# 무한대 값 설정 (충분히 큰 값)
INF = float('inf')

# 입력 받기
n, m = map(int, input().split())
dist = [[INF] * n for _ in range(n)]

# 자기 자신으로의 거리는 0으로 초기화
for i in range(n):
    dist[i][i] = 0

# 친구 관계 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1  # 인덱스 0부터 시작하도록 조정
    b -= 1
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드-와샬 알고리즘 수행
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 케빈 베이컨 수가 가장 작은 유저 찾기
min_bacon = INF
min_person = 0

for i in range(n):
    bacon_sum = sum(dist[i])
    if bacon_sum < min_bacon:
        min_bacon = bacon_sum
        min_person = i

# 유저 번호는 1부터 시작하므로 결과에 +1
print(min_person + 1)
